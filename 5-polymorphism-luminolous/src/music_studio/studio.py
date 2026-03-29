from __future__ import annotations
from typing import List
from .instrumen import Instrumen, Gitar, Piano

class StudioMusik:
    def __init__(self) -> None:
        self._list_instrumen: List[Instrumen] = []

    def tambah_instrumen(self, instrumen: Instrumen) -> None:
        if not isinstance(instrumen, Instrumen):
            raise TypeError("Parameter harus objek turunan Instrumen")
        self._list_instrumen.append(instrumen)

    def mainkan_instrumen(self) -> list[str]:
        hasil: list[str] = []
        for ins in self._list_instrumen:
            hasil.append(f"{ins.nama} berbunyi: {ins.mainkan()}")
        return hasil


if __name__ == "__main__":
    studio = StudioMusik()
    g1 = Gitar("Gitar Akustik")
    p1 = Piano("Grand Piano")

    studio.tambah_instrumen(g1)
    studio.tambah_instrumen(p1)

    for line in studio.mainkan_instrumen():
        print(line)