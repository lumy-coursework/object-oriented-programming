from __future__ import annotations
from typing import List
from .hewan import Hewan, Kucing, Anjing

class ParadeHewan:
    def __init__(self) -> None:
        self._list_hewan: List[Hewan] = []

    def tambah_hewan(self, hewan: Hewan) -> None:
        if not isinstance(hewan, Hewan):
            raise TypeError("Parameter harus objek turunan Hewan")
        self._list_hewan.append(hewan)

    def hapus_hewan(self, hewan: Hewan) -> None:
        if hewan in self._list_hewan:
            self._list_hewan.remove(hewan)

    def mulai_parade(self, putaran: int) -> list[str]:
        if not isinstance(putaran, int):
            raise TypeError("putaran harus int")
        if putaran < 1:
            raise ValueError("putaran harus >= 1")

        hasil: list[str] = []
        for _ in range(putaran):
            for hewan in self._list_hewan:
                hasil.append(f"{hewan.nama} bersuara: {hewan.bersuara()}")
        return hasil


if __name__ == "__main__":
    parade = ParadeHewan()
    k1 = Kucing("Momo")
    a1 = Anjing("Bobby")
    parade.tambah_hewan(k1)
    parade.tambah_hewan(a1)

    output = parade.mulai_parade(2)
    for line in output:
        print(line)