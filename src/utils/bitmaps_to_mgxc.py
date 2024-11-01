from typing import List
import numpy as np

from utils.note_primitive import Note
from utils.event_primitive import TIL, Event

NOTE_INTERVAL = 5
BAR_INTERVAL = 1920
BEAT_INTERVAL = BAR_INTERVAL // 4


SPEED = 100.0
SPEED_MAX = 1000000.0
SPEED_MIN = 0.0


def bitmaps_to_mgxc(
    bitmaps: List[np.ndarray], on: Note, off: Note, frame_cap: int = -1
) -> tuple[List[Note], List[Event]]:
    notes = []
    events = []

    for i, bitmap in enumerate(bitmaps):
        events.append(TIL(i * BEAT_INTERVAL, SPEED))
        for j, row in enumerate(bitmap):
            for k, bit in enumerate(row):
                if bit:
                    notes.append(on(i * BEAT_INTERVAL + j * NOTE_INTERVAL, k, 1))
                else:
                    notes.append(off(i * BEAT_INTERVAL + j * NOTE_INTERVAL, k, 1))

        events.append(TIL(i * BEAT_INTERVAL + (j + 1) * NOTE_INTERVAL, SPEED_MAX))
        events.append(TIL(i * BEAT_INTERVAL + (j + 3) * NOTE_INTERVAL, SPEED_MIN))

        if frame_cap > 0 and i >= frame_cap:
            break

    return notes, events
