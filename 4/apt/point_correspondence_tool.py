"""Simple A.2 point-correspondence visualizer.

Edit the image paths and point arrays below, then run:

    python point_correspondence_tool.py

The figure is displayed and saved automatically as a PNG.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


# Change these paths if you want to use different images.
SOURCE_IMAGE = "img/apt/left_d.jpg"
TARGET_IMAGE = "img/apt/right_d.jpg"
SOURCE_OUTPUT = "out/source_correspondences.png"
TARGET_OUTPUT = "out/target_correspondences.png"


# Add or remove matching points here.
# Point order must match: source point 1 corresponds to target point 1, etc.
SOURCE_POINTS = np.array(
    [
        [587,497],[595,585],[658,635],[550,363],[653,421],[599,671]
    ],
    dtype=float,
)

TARGET_POINTS = np.array(
    [
        [40,502],[32,594],[87,644],[22,357],[118,435],[16,685]
    ],
    dtype=float,
)


def draw_points(axis, image, points, title):
    """Show one image with numbered correspondence points."""
    axis.imshow(image)
    axis.axis("off")

    for number, (x, y) in enumerate(points, start=1):
        axis.scatter(x, y, s=90, c="red", edgecolors="white", linewidths=1.5)
        axis.text(
            x + 10,
            y - 10,
            str(number),
            color="yellow",
            fontsize=12,
            fontweight="bold",
            bbox={"facecolor": "black", "alpha": 0.65, "pad": 2},
        )


def save_single_image(image, points, title, output_path):
    """Save one image with its numbered correspondence points."""
    height, width = image.shape[:2]
    figure, axis = plt.subplots(figsize=(width / 100, height / 100), dpi=100)
    draw_points(axis, image, points, title)
    figure.subplots_adjust(left=0, right=1, bottom=0, top=1)
    figure.savefig(output_path, dpi=100, pad_inches=0)
    plt.close(figure)


def main():
    if len(SOURCE_POINTS) != len(TARGET_POINTS):
        raise ValueError("SOURCE_POINTS and TARGET_POINTS must have the same length.")

    source = mpimg.imread(SOURCE_IMAGE)
    target = mpimg.imread(TARGET_IMAGE)

    output_folder = Path(SOURCE_OUTPUT).parent
    output_folder.mkdir(parents=True, exist_ok=True)

    save_single_image(source, SOURCE_POINTS, "Source image", SOURCE_OUTPUT)
    save_single_image(target, TARGET_POINTS, "Target image", TARGET_OUTPUT)

    figure, axes = plt.subplots(1, 2, figsize=(14, 7))
    draw_points(axes[0], source, SOURCE_POINTS, "Source image")
    draw_points(axes[1], target, TARGET_POINTS, "Target image")
    figure.tight_layout()

    print(f"Saved source image to: {SOURCE_OUTPUT}")
    print(f"Saved target image to: {TARGET_OUTPUT}")

    plt.show()


if __name__ == "__main__":
    main()
