from __future__ import annotations
from typing import List
from .karya_seni import KaryaSeni, Lukisan, Patung

class StudioSeni:
    def __init__(self) -> None:
        self._list_karya: List[KaryaSeni] = []

    def tambah_karya_seni(self, karya: KaryaSeni) -> None:
        if not isinstance(karya, KaryaSeni):
            raise TypeError("Parameter harus turunan KaryaSeni")
        self._list_karya.append(karya)

    def tampilkan_semua_karya(self) -> list[str]:
        return [k.tampilkan() for k in self._list_karya]


if __name__ == "__main__":
    studio = StudioSeni()
    l1 = Lukisan("Monalisa KW")
    p1 = Patung("Patung Dada Batu")

    studio.tambah_karya_seni(l1)
    studio.tambah_karya_seni(p1)

    for karya in [l1, p1]:
        print(f"{karya.judul}: {karya.deskripsi()}")

    print("Cara display di studio:")
    for line in studio.tampilkan_semua_karya():
        print("-", line)