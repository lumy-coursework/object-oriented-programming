from __future__ import annotations
from typing import Any, List
from .lingkaran import Lingkaran
from .persegi import Persegi
from .segitiga import Segitiga
from .bukan_bentuk import BukanBentuk

class ShapeRenderer:
    def __init__(self) -> None:
        self._bentuk: List[Any] = []

    def tambah_bentuk(self, bentuk: Any) -> None:
        self._bentuk.append(bentuk)

    def render_semua(self) -> list[str]:
        hasil: list[str] = []
        for obj in self._bentuk:
            if hasattr(obj, "render") and callable(getattr(obj, "render")):
                try:
                    out = obj.render()
                except TypeError:
                    continue
                hasil.append(str(out))
        return hasil


if __name__ == "__main__":
    renderer = ShapeRenderer()
    renderer.tambah_bentuk(Lingkaran(5))
    renderer.tambah_bentuk(Persegi(4))
    renderer.tambah_bentuk(Segitiga(3, 6))
    renderer.tambah_bentuk(BukanBentuk())

    for line in renderer.render_semua():
        print(line)