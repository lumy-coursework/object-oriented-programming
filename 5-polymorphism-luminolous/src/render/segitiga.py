from __future__ import annotations

def _fmt(num: float) -> str:
    if isinstance(num, (int,)) or (isinstance(num, float) and num.is_integer()):
        return str(int(num))
    return str(num)

class Segitiga:
    def __init__(self, alas: float, tinggi: float) -> None:
        self._alas = 0.0
        self._tinggi = 0.0
        self.alas = alas    
        self.tinggi = tinggi

    @property
    def alas(self) -> float:
        return self._alas

    @alas.setter
    def alas(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("alas harus numerik")
        if value <= 0:
            raise ValueError("alas harus > 0")
        self._alas = float(value)

    @property
    def tinggi(self) -> float:
        return self._tinggi

    @tinggi.setter
    def tinggi(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("tinggi harus numerik")
        if value <= 0:
            raise ValueError("tinggi harus > 0")
        self._tinggi = float(value)

    def render(self) -> str:
        return f"Render Segitiga (a={_fmt(self.alas)}, t={_fmt(self.tinggi)})"