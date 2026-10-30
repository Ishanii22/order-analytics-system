import json
import re
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

pattern = r'const API = "http://127\.0\.0\.1:8000";'
if not re.search(pattern, html):
    raise SystemExit("API line not found in dashboard.html")

demo_js = (
    'const API = "http://127.0.0.1:8000";\n'
    f'const DEMO_DATA = {json.dumps(data)};\n'
    'window.fetch = async (url) => ({ ok: true, json: async () => DEMO_DATA[url.replace(API, "")] });'
)
html = re.sub(pattern, lambda m: demo_js, html, count=1)

html = html.replace('"Connected to API"', '"Demo snapshot"')
html = html.replace(
    "Sales, stock and orders from the FastAPI + PostgreSQL backend",
    "Static demo: a snapshot of data from the FastAPI + PostgreSQL backend",
)

# 4. Save to docs/index.html (the folder GitHub Pages serves)
Path("docs").mkdir(exist_ok=True)
Path("docs/index.html").write_text(html, encoding="utf-8")
print("✅ docs/index.html updated")