from typing import List
from utils.bitmaps_to_notes import bitmaps_to_notes
from utils.event_primitive import Beat, BPM, Event
from utils.video_to_bitmaps import video_to_bitmaps
from utils.note_primitive import Damage, Tap, Note


def write_chart(events: List[Event], notes: List[Note], path: str) -> None:
    with open("res/template.mgxc", "r", encoding="utf-8") as f:
        template = f.read().strip().split("\n")

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(template))
        f.write("\n")
        f.write("\n".join([str(event) for event in events]))
        f.write("\n")

        f.writelines("BEGIN\tNOTES")
        f.write("\n")
        f.write("\n".join([str(note) for note in notes]))
        f.write("\n")


if __name__ == "__main__":
    video_path = "res/bad_apple.mp4"
    target_width = 16
    target_fps = 30.0

    fps, bitmaps = video_to_bitmaps(video_path, target_width, target_fps)
    default_events = [Beat(0, 4, 4), BPM(0, fps * 60)]

    notes, events = bitmaps_to_notes(bitmaps, Damage, Tap, 600)
    write_chart(default_events + events, notes, "out/bad_apple_partial.mgxc")

    notes, events = bitmaps_to_notes(bitmaps, Damage, Tap)
    write_chart(default_events + events, notes, "out/bad_apple_full.mgxc")
