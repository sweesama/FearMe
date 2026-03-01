import os, json, sys
from urllib.request import urlretrieve, Request, urlopen
from urllib.parse import quote
from urllib.error import URLError

BASE = "https://html-classic.itch.zone/html/16183209/"
OUT = "."
SKIP = {"game.zip", "index.html", "index.html.symbols", "manifest.json", "renpy-pre.js", "renpy.data", "renpy.js", "renpy.wasm", "service-worker.js", "web-presplash.jpg", "pwa_catalog.json", "download.ps1", "download_assets.py"}

with open("pwa_catalog.json", "r") as f:
    catalog = json.load(f)

files = [x for x in catalog["files"] if x not in SKIP]
print(f"Need to download {len(files)} files", flush=True)

ok = 0
fail = 0
for i, fname in enumerate(files):
    out_path = os.path.join(OUT, fname)
    if os.path.exists(out_path) and os.path.getsize(out_path) > 100:
        ok += 1
        continue
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    url = BASE + quote(fname, safe="/")
    try:
        urlretrieve(url, out_path)
        ok += 1
    except Exception as e:
        fail += 1
        print(f"FAIL [{i+1}]: {fname} -> {e}", flush=True)
    if (i+1) % 30 == 0:
        print(f"Progress: {i+1}/{len(files)} (ok={ok} fail={fail})", flush=True)

print(f"\nDONE: {ok} ok, {fail} failed out of {len(files)}", flush=True)
