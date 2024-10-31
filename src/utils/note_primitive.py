class Tap: # red
    def __init__(self, tick: int, lane: int, width: int) -> None:
        self.tick: int = tick
        self.lane: int = lane
        self.width: int = width

    def __str__(self) -> str:
        return f"t\tN\tN\tN\t{self.tick}\t{self.lane}\t{self.width}\t8\t0\t0"


class ExTap(Tap): # yellow
    def __str__(self) -> str:
        return f"e\tN\tU\tN\t{self.tick}\t{self.lane}\t{self.width}\t8\t0\t0"


class Flick(Tap): # cyan
    def __str__(self) -> str:
        return f"f\tN\tA\tN\t{self.tick}\t{self.lane}\t{self.width}\t8\t0\t0"


class Damage(Tap): # dark blue
    def __str__(self) -> str:
        return f"d\tN\tN\tN\t{self.tick}\t{self.lane}\t{self.width}\t8\t0\t0"
    
class Hold(Tap): # orange
    def __str__(self) -> str:
        return (
            f"h\tBG\tN\tN\t{self.tick}\t{self.lane}\t{self.width}\t8\t0\t0\n"
            f".h\tEN\tN\tN\t{self.tick+5}\t{self.lane}\t{self.width}\t8\t0\t0"
        )
        
class Slide(Tap): # blue
    def __str__(self) -> str:
        return (
            f"s\tBG\tN\tN\t{self.tick}\t{self.lane}\t{self.width}\t8\t0\t0\n"
            f".s\tEN\tN\tN\t{self.tick+5}\t{self.lane}\t{self.width}\t8\t0\t0"
        )

class Crush(Damage): # purple
    def __str__(self) -> str:
        return (
            f"C\tBG\tN\tAT\t{self.tick}\t{self.lane}\t{self.width}\t0\t0\t35\n"
            f".C\tEN\tN\tN\t{self.tick+10}\t{self.lane}\t{self.width}\t0\t0\t0"
        )
