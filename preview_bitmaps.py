import os
import sys
import time
import pickle


def clear_console_ansi():
    sys.stdout.write("\033[H")
    sys.stdout.flush()


def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def bitmap_to_string(bitmap):
    ON = "-"
    OFF = " "

    lines = []
    for row in bitmap:
        line = "".join([ON if pixel else OFF for pixel in row])
        lines.append(line)
    return "\n".join(lines)


def preview_bitmaps(fps, bitmaps):
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
    with open("bitmaps.pkl", "rb") as f:
        fps, bitmaps = pickle.load(f)
    clear_console()
    preview_bitmaps(fps, bitmaps)
