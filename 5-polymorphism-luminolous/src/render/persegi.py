from __future__ import annotations

def _fmt(num: float) -> str:
    if isinstance(num, (int,)) or (isinstance(num, float) and num.is_integer()):
        return str(int(num))
    return str(num)

class Persegi:
    def __init__(self, sisi: float) -> None:
        self._sisi = 0.0
        self.sisi = sisi

    @property
    def sisi(self) -> float:
        return self._sisi

    @sisi.setter
    def sisi(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("sisi harus numerik")
        if value <= 0:
            raise ValueError("sisi harus > 0")
        self._sisi = float(value)

    def render(self) -> str:
        return f"Render Persegi (s={_fmt(self.sisi)})"