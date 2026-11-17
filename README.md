# Child Growth Assessment — Vercel Web App

Next.js frontend + Python/Flask API using the WHO Anthro methodology.

## Deploy

1. Extract this ZIP.
2. Go to Vercel and choose **Vercel Drop**, or connect the folder through GitHub.
3. Upload/import the project.
4. Vercel detects Next.js. Deploy with defaults.

## Local

npm install
npm run dev

The Python API requires Flask and anthro; Vercel installs them from `api/requirements.txt`.

## Important
This is an independent WHO-based implementation, not official Poshan Tracker software. Validate against the exact Poshan Tracker release before healthcare/government use. Under-2 measurement technique (recumbent length vs standing height) needs particular validation.


## Vercel fix
This version includes `pyproject.toml` with `[tool.vercel] entrypoint = "api.calculate:app"` and upgrades Next.js to 16.4.6.
