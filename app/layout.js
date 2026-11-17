import './globals.css';
export const metadata={title:'Child Growth Assessment',description:'WHO-based child growth screening',manifest:'/manifest.webmanifest',applicationName:'Growth Assessment'};
export const viewport={themeColor:'#0f766e',width:'device-width',initialScale:1};
export default function Layout({children}){return <html lang="en"><body>{children}</body></html>}
