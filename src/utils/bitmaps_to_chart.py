from typing import List
import numpy as np

from utils.note_primitive import Note
from utils.event_primitive import TIL, Event, Beat, BPM

OFFSET = 1920
INTERVAL = 5

BAR_INTERVAL = 1920
BEAT_INTERVAL = BAR_INTERVAL // 4

SPEED = 100.0
SPEED_MAX = 1000000.0
SPEED_MIN = 0.0


def bitmaps_to_chart(
    fps: float,
    bitmaps: List[np.ndarray],
    on: Note,
    off: Note,
    frame_start: int = -1,
    frame_end: int = -1,
) -> tuple[List[Note], List[Event]]:
    notes, events = [], [Beat(0, 4, 4), BPM(0, fps * 60)]

    frame_start = 0 if frame_start < 0 else frame_start
    frame_end = len(bitmaps) if frame_end <= frame_start else frame_end

    for i, bitmap in enumerate(bitmaps):
        if i < frame_start:
            continue

        if i > frame_end:
            break

        base_time = i * BEAT_INTERVAL + OFFSET
        events.append(TIL(base_time, SPEED))

        for j, row in enumerate(bitmap):
            time = base_time + j * INTERVAL
            for k, bit in enumerate(row):
                notes.append(on(time, k, 1) if bit else off(time, k, 1))

        events.append(TIL(time + INTERVAL, SPEED_MAX))
        events.append(TIL(time + 2 * INTERVAL, SPEED_MIN))

    return notes, events
