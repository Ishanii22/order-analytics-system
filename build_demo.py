import json
import urllib.request
from pathlib import Path

API = "http://127.0.0.1:8000"
ENDPOINTS = ["/products/", "/orders/", "/customers/", "/analytics/daily-sales"]

# 1. Fetch live data from the running API
data = {}
for ep in ENDPOINTS:
    with urllib.request.urlopen(API + ep) as r:
        data[ep] = json.loads(r.read().decode())

# 2. Remove test data created by pytest
data["/products/"] = [p for p in data["/products/"] if p["name"] != "Test Product"]
data["/customers/"] = [c for c in data["/customers/"] if c["name"] != "Test Customer"]

# 3. Embed the data into a copy of dashboard.html
html = Path("dashboard.html").read_text(encoding="utf-8")

marker = 'const API_BASE = "http://127.0.0.1:8000";'
if marker not in html:
    raise SystemExit("API_BASE line not found in dashboard.html")

demo_js = f'''const API_BASE = "http://127.0.0.1:8000";
const DEMO_DATA = {json.dumps(data)};
window.fetch = async (url) => ({{ json: async () => DEMO_DATA[url.replace(API_BASE, "")] }});'''

html = html.replace(marker, demo_js)
html = html.replace("Live data from FastAPI backend", "Static demo - snapshot of data from the FastAPI backend")
html = html.replace('s.date.split("T")[0]', 's.date.split(" ")[0]')

# 4. Save to docs/index.html (GitHub Pages folder)
Path("docs").mkdir(exist_ok=True)
Path("docs/index.html").write_text(html, encoding="utf-8")
print("✅ docs/index.html created")