from pathlib import Path
import json
import sys

try:
    import nbformat
except ImportError:
    print("Install karo: python -m pip install nbformat")
    sys.exit(1)

bad = []
suspicious = []
good = 0

for p in sorted(Path(".").rglob("*.ipynb")):
    if ".git" in p.parts or ".ipynb_checkpoints" in p.parts:
        continue

    size_mb = p.stat().st_size / 1024 / 1024

    try:
        raw = p.read_text(encoding="utf-8")
        json.loads(raw)  # broken JSON catch karega
        nb = nbformat.reads(raw, as_version=4)
        nbformat.validate(nb)
    except Exception as e:
        bad.append(
            (
                str(p),
                f"{size_mb:.2f} MB",
                type(e).__name__,
                str(e).splitlines()[0][:180],
            )
        )
        continue

    outputs = 0
    output_bytes = 0

    for cell in nb.cells:
        for out in cell.get("outputs", []):
            outputs += 1
            output_bytes += len(json.dumps(out, ensure_ascii=False))

    output_mb = output_bytes / 1024 / 1024
    has_widgets = "widgets" in nb.get("metadata", {})

    if size_mb > 5 or output_mb > 3 or has_widgets:
        suspicious.append(
            (
                str(p),
                f"{size_mb:.2f} MB",
                f"{outputs} outputs",
                f"{output_mb:.2f} MB outputs",
                "widgets" if has_widgets else "",
            )
        )
    else:
        good += 1

print("\n=== CORRUPT / INVALID NOTEBOOKS ===")
if not bad:
    print("None")
else:
    for item in bad:
        print(" | ".join(item))

print("\n=== SUSPICIOUS NOTEBOOKS ===")
print("Ye corrupt nahi hain, lekin GitHub renderer inki wajah se fail ho sakta hai.")
if not suspicious:
    print("None")
else:
    for item in suspicious:
        print(" | ".join(item))

print("\n=== SUMMARY ===")
print(f"Good notebooks: {good}")
print(f"Corrupt/invalid notebooks: {len(bad)}")
print(f"Suspicious/heavy notebooks: {len(suspicious)}")