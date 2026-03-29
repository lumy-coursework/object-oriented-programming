from __future__ import annotations

def _fmt(num: float) -> str:
    if isinstance(num, (int,)) or (isinstance(num, float) and num.is_integer()):
        return str(int(num))
    return str(num)


class Lingkaran:
    def __init__(self, radius: float) -> None:
        self._radius = 0.0
        self.radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("radius harus numerik")
        if value <= 0:
            raise ValueError("radius harus > 0")
        self._radius = float(value)

    def render(self) -> str:
        return f"Render Lingkaran (r={_fmt(self.radius)})"