from pathlib import Path
import re
import uuid
import nbformat

ID_RE = re.compile(r"^[A-Za-z0-9_-]+$")

# Is file ke heavy outputs GitHub renderer crash kar rahe thay
CLEAR_OUTPUTS_FILE = Path(r"Machine Learning\plotly\pandas_profiling.ipynb")


def make_cell_id():
    return uuid.uuid4().hex[:8]


def is_valid_cell_id(value, seen):
    return (
        isinstance(value, str)
        and 1 <= len(value) <= 64
        and ID_RE.fullmatch(value) is not None
        and value not in seen
    )


changed_files = []
failed_files = []

for p in sorted(Path(".").rglob("*.ipynb")):
    if ".git" in p.parts or ".ipynb_checkpoints" in p.parts:
        continue

    try:
        nb = nbformat.read(str(p), as_version=4)
        changed = False

        # Cell id ko valid banane ke liye notebook minor version 5 hona chahiye
        nb["nbformat"] = 4

        try:
            minor = int(nb.get("nbformat_minor", 0) or 0)
        except Exception:
            minor = 0

        if minor < 5:
            nb["nbformat_minor"] = 5
            changed = True

        # Missing / duplicate / invalid cell IDs fix karo
        seen = set()
        for cell in nb.get("cells", []):
            old_id = cell.get("id")

            if not is_valid_cell_id(old_id, seen):
                new_id = make_cell_id()
                while new_id in seen:
                    new_id = make_cell_id()

                cell["id"] = new_id
                changed = True

            seen.add(cell["id"])

        # Sirf pandas_profiling notebook ke heavy outputs clear karo
        same_file = (
            p == CLEAR_OUTPUTS_FILE
            or str(p).replace("/", "\\").endswith(
                r"Machine Learning\plotly\pandas_profiling.ipynb"
            )
        )

        if same_file:
            for cell in nb.get("cells", []):
                if cell.get("cell_type") == "code":
                    if cell.get("outputs"):
                        cell["outputs"] = []
                        changed = True

                    if cell.get("execution_count") is not None:
                        cell["execution_count"] = None
                        changed = True

            if "widgets" in nb.get("metadata", {}):
                nb["metadata"].pop("widgets", None)
                changed = True

        # Validate before saving
        nbformat.validate(nb)

        if changed:
            nbformat.write(nb, str(p))
            changed_files.append(str(p))

    except Exception as e:
        failed_files.append(
            (str(p), type(e).__name__, str(e).splitlines()[0][:200])
        )

print("\n=== CHANGED FILES ===")
if changed_files:
    for f in changed_files:
        print(f)
else:
    print("None")

print("\n=== FAILED FILES ===")
if failed_files:
    for f, err_type, msg in failed_files:
        print(f"{f} | {err_type} | {msg}")
else:
    print("None")

print(f"\nDone. Changed: {len(changed_files)}, Failed: {len(failed_files)}")