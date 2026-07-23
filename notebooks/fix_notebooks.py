import json
from pathlib import Path

for path in Path(".").glob("*.ipynb"):
    with path.open("r", encoding="utf-8") as file:
        notebook = json.load(file)

    widgets = notebook.get("metadata", {}).pop("widgets", None)

    if widgets is not None:
        with path.open("w", encoding="utf-8") as file:
            json.dump(notebook, file, ensure_ascii=False, indent=1)
            file.write("\n")

        print(f"Fixed: {path.name}")
    else:
        print(f"Already valid: {path.name}")
