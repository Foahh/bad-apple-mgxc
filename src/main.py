from typing import List
from utils.bitmaps_to_chart import bitmaps_to_chart
from utils.event_primitive import Event
from utils.video_to_bitmaps import video_to_bitmaps
from utils.note_primitive import Damage, Tap, Note, ExTap


def write_chart(
    template: str, notes: List[Note], events: List[Event], path: str
) -> None:
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(template)
        f.write("\n")

        f.writelines("BEGIN\tHEADER\n")
        f.write("\n".join([str(event) for event in events]))
        f.write("\n")

        f.writelines("BEGIN\tNOTES\n")
        f.write("\n".join([str(note) for note in notes]))
        f.write("\n")


def format(template: str, parameter: dict) -> str:
    for key, value in parameter.items():
        template = template.replace("{{" + key + "}}", value)
        return template


if __name__ == "__main__":
    video_path = "res/bad_apple.mp4"
    target_width = 16
    target_fps = 30.0
    result = video_to_bitmaps(video_path, target_width, target_fps)

    with open("res/template.mgxc", "r", encoding="utf-8") as f:
        template = f.read()

    chart = bitmaps_to_chart(*result, ExTap, Tap)
    header = format(template, {"INDEX": "FULL"})
    write_chart(header, *chart, "out/bad_apple_full.mgxc")

    size = len(result[1]) // 15
    print(f"切片大小：{size}")
    for i in range(15):
        header = format(template, {"INDEX": f"{i + 1:02d}"})
        chart = bitmaps_to_chart(*result, ExTap, Tap, i * size, (i + 1) * size)
        write_chart(header, *chart, f"out/bad_apple_{i + 1:02d}.mgxc")
