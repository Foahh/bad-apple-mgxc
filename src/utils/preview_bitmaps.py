import os
import sys
import time
from typing import List
import numpy as np

from utils.video_to_bitmaps import video_to_bitmaps


def clear_console_ansi() -> None:
    sys.stdout.write("\033[H")
    sys.stdout.flush()


def clear_console() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def bitmap_to_string(bitmap: List[np.ndarray]) -> None:
    ON = "-"
    OFF = " "

    lines = []
    for row in bitmap:
        line = "".join([ON if pixel else OFF for pixel in row])
        lines.append(line)
    return "\n".join(lines)


def preview_bitmaps(fps: float, bitmaps: List[np.ndarray]) -> None:
    frame_duration = 1 / fps

    try:
        while True:
            for bitmap in bitmaps:
                clear_console_ansi()
                print(bitmap_to_string(bitmap))
                time.sleep(frame_duration)
    except KeyboardInterrupt:
        clear_console()


if __name__ == "__main__":
    video_path = "res/bad_apple.mp4"
    target_width = 16
    target_fps = 30.0
    fps, bitmaps = video_to_bitmaps(video_path, target_width, target_fps)

    clear_console()
    preview_bitmaps(fps, bitmaps)
