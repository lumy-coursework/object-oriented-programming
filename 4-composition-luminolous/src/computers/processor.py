from __future__ import annotations

class Processor:
    def __init__(self, brand: str, speed: float) -> None:
        self.brand = brand
        self.speed = speed

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, value: str) -> None:
        self._brand = (value or "").strip()

    @property
    def speed(self) -> float:
        return self._speed

    @speed.setter
    def speed(self, value: float) -> None:
        self._speed = float(value)

    def __repr__(self) -> str:
        return f"Processor(brand={self._brand!r}, speed={self._speed} GHz)"

if __name__ == "__main__":
    p = Processor("Intel", 3.6)
    print(p)
    p.brand = "AMD"
    p.speed = 4.2
    print("Brand:", p.brand, "| Speed:", p.speed, "GHz")