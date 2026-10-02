# /// script
# requires-python = ">=3.11"
# dependencies = ["resvg-py==0.5.0", "pillow==12.3.0"]
# ///
"""Render every icon from the sole SVG master; optionally sync the local app."""

import argparse
from io import BytesIO
from pathlib import Path
from shutil import copyfile

import resvg_py
from PIL import Image

SITE = Path(__file__).resolve().parents[1]
BRANDING = SITE / "assets" / "branding"
MASTER = BRANDING / "content-factory-icon.svg"
SIZES = {
    "favicon-16x16.png": 16,
    "favicon-32x32.png": 32,
    "apple-touch-icon.png": 180,
    "content-factory-icon-192.png": 192,
    "content-factory-icon-512.png": 512,
    "content-factory-tiktok-app-icon.png": 1024,
}


def render(size):
    png = resvg_py.svg_to_bytes(
        svg_path=str(MASTER), width=size, height=size, skip_system_fonts=True
    )
    return Image.open(BytesIO(png)).convert("RGB")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--app-static", type=Path, help="Content Factory web/static directory")
    args = parser.parse_args()
    for filename, size in SIZES.items():
        render(size).save(BRANDING / filename, optimize=True)
        print(f"{filename}: {size} × {size}")
    # Every ICO frame is rendered from the same SVG, without a favicon-only redesign.
    render(48).save(
        BRANDING / "favicon.ico",
        sizes=[(16, 16), (32, 32), (48, 48)],
        append_images=[render(16), render(32)],
    )
    copyfile(BRANDING / "favicon.ico", SITE / "favicon.ico")
    if args.app_static:
        destination = args.app_static.resolve() / "branding"
        destination.mkdir(parents=True, exist_ok=True)
        for filename in [MASTER.name, *SIZES, "favicon.ico"]:
            copyfile(BRANDING / filename, destination / filename)
        print(f"Identical generated assets copied to {destination}")


if __name__ == "__main__":
    main()
