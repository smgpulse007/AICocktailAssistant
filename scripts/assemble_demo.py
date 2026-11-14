"""Assemble the README GIF from actual Playwright browser screenshots."""
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
from pathlib import Path
import platform

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]


def main():
    paths = [ROOT / "output/playwright" / f"gif-{number:02}.png" for number in range(1, 5)]
    frames = [Image.open(path).convert("RGB") for path in paths]
    if len({frame.size for frame in frames}) != 1:
        raise ValueError("Browser frames must share a viewport size")
    output = ROOT / "docs/cocktail-demo.gif"
    output.parent.mkdir(exist_ok=True)
    durations = [2000, 4500, 2500, 3500]
    frames[0].save(output, save_all=True, append_images=frames[1:], duration=durations,
                   loop=0, disposal=2, optimize=True)
    sources = ["app.py", "recommendation_engine.py", "data_preparation.py", "ingredients.json", "recipes.json"]
    digest = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
    metadata = {
        "recorded_utc": datetime.now(timezone.utc).isoformat(),
        "method": "Actual local Streamlit app screenshots; Playwright CLI with isolated Microsoft Edge",
        "viewport": list(frames[0].size),
        "inputs": ["Negroni", "negroni", "Negroni"],
        "frame_durations_ms": durations,
        "source_sha256": {name: digest(ROOT / name) for name in sources},
        "frame_sha256": {path.name: digest(path) for path in paths},
        "gif_sha256": digest(output),
        "python": platform.python_version(),
        "packages": {name: importlib.metadata.version(name) for name in ("streamlit", "numpy", "pandas", "scikit-learn")},
    }
    (ROOT / "docs/demo-recording.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {output.relative_to(ROOT)} ({output.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
