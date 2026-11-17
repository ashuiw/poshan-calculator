from datetime import date, datetime
from flask import Flask, request, jsonify
from anthro import compute

app = Flask(__name__)

def st(z, mod, severe):
    if z is None:
        return "Not available"
    if z < -3:
        return severe
    if z < -2:
        return mod
    return "Normal"

@app.post("/api/calculate")
def calculate():
    try:
        d = request.get_json(force=True)
        dob = datetime.strptime(d["dob"], "%Y-%m-%d").date()
        measured = datetime.strptime(d.get("measured") or date.today().isoformat(), "%Y-%m-%d").date()
        sex = d["sex"].lower()
        w = float(d["weight"])
        h = float(d["height"])
        if sex not in ("male", "female"):
            raise ValueError("Sex must be male or female.")
        if w <= 0 or h <= 0:
            raise ValueError("Weight and height must be greater than zero.")
        if measured < dob:
            raise ValueError("Measurement date cannot be before date of birth.")
        age = (measured - dob).days
        r = compute({"sex": sex, "age_days": age, "weight_kg": w, "height_cm": h})
        hfa, wfa, wfh = r.get("z_lhfa"), r.get("z_wfa"), r.get("z_wflh")
        wasting = st(wfh, "MAM", "SAM")
        if age >= int(5 * 365.25 + 1):
            wasting = "Not assessed (wasting reference ends at 5 years)"
        return jsonify({
            "sex": sex, "age_days": age, "age_months": round(age / 30.4375, 2),
            "stunting": st(hfa, "Moderately Stunted", "Severely Stunted"),
            "underweight": st(wfa, "Moderately Underweight", "Severely Underweight"),
            "wasting": wasting,
            "z_hfa": None if hfa is None else round(float(hfa), 2),
            "z_wfa": None if wfa is None else round(float(wfa), 2),
            "z_wfh": None if wfh is None else round(float(wfh), 2)
        })
    except KeyError as e:
        return jsonify(error=f"Missing field: {e.args[0]}"), 400
    except Exception as e:
        return jsonify(error=str(e)), 400
