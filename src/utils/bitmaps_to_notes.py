from typing import List
import numpy as np

from utils.note_primitive import Note
from utils.event_primitive import TIL, Event

OFFSET = 1920
INTERVAL = 5

BAR_INTERVAL = 1920
BEAT_INTERVAL = BAR_INTERVAL // 4

SPEED = 100.0
SPEED_MAX = 1000000.0
SPEED_MIN = 0.0


def bitmaps_to_notes(
    bitmaps: List[np.ndarray], on: Note, off: Note, frame_cap: int = -1
) -> tuple[List[Note], List[Event]]:
    notes, events = [], []

    for i, bitmap in enumerate(bitmaps):
        base_time = i * BEAT_INTERVAL + OFFSET
        events.append(TIL(base_time, SPEED))

        for j, row in enumerate(bitmap):
            time = base_time + j * INTERVAL
            notes.extend(
                [
                    on(time, k, 1) if bit else off(time, k, 1)
                    for k, bit in enumerate(row)
                ]
            )

        events.extend(
            [
                TIL(time + INTERVAL, SPEED_MAX),
                TIL(time + 3 * INTERVAL, SPEED_MIN),
            ]
        )

        if frame_cap > 0 and i >= frame_cap:
            break

    return notes, events
