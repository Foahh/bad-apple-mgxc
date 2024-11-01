class Event:
    def __init__(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError


class TIL(Event):
    def __init__(self, tick: int, speed: float):
        self.tick: int = tick
        self.speed: float = speed

    def __str__(self):
        return f"TIL\t0\t{self.tick}\t{self.speed:.5f}"


class BPM(Event):
    def __init__(self, tick: int, bpm: float):
        self.tick: int = tick
        self.bpm: float = bpm

    def __str__(self):
        return f"BPM\t{self.tick}\t{self.bpm:.5f}"


class Beat(Event):
    def __init__(self, bar: int, numerator: int, denominator: int):
        self.bar: int = bar
        self.numerator: int = numerator
        self.denominator: int = denominator

    def __str__(self):
        return f"BEAT\t{self.bar}\t{self.numerator}\t{self.denominator}"
