from typing import List
from utils.bitmaps_to_chart import bitmaps_to_chart
from utils.event_primitive import Event
from utils.video_to_bitmaps import video_to_bitmaps
from utils.note_primitive import Damage, Note, Crush, Tap, Flick


def write_chart(
    template: str, notes: List[Note], events: List[Event], path: str
) -> None:
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(template)
        f.write("\n")

        f.writelines("BEGIN\tHEADER\n")
        f.write("\n".join([str(event) for event in events if event is not None]))
        f.write("\n")

        f.writelines("BEGIN\tNOTES\n")
        f.write("\n".join([str(note) for note in notes if note is not None]))
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

    bits = (Damage, Crush)

    chart = bitmaps_to_chart(*result, *bits)
    header = format(template, {"INDEX": "FULL"})
    write_chart(header, *chart, "out/bad_apple_full.mgxc")

    segment = 10
    size = len(result[1]) // segment
    print(f"切片数量：{segment}，大小：{size} 帧")
    for i in range(segment):
        header = format(template, {"INDEX": f"{i + 1:02d}"})
        chart = bitmaps_to_chart(*result, *bits, i * size, (i + 1) * size)
        write_chart(header, *chart, f"out/bad_apple_{i + 1:02d}.mgxc")
