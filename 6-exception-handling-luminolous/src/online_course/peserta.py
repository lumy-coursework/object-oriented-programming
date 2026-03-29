from __future__ import annotations

from .exceptions import (
    UsiaTidakMemenuhiSyaratError,
    PendidikanTidakMemenuhiSyaratError,
)


class Peserta:
    def __init__(self, nama: str, usia: int, tingkat_pendidikan: str) -> None:
        # Validasi nama
        if not isinstance(nama, str) or nama.strip() == "":
            raise ValueError("Nama peserta harus berupa string non-kosong")

        # Validasi usia (harus int)
        if not isinstance(usia, int):
            raise ValueError("Usia harus berupa integer")

        self._nama: str = nama
        self._usia: int = usia
        self._tingkat_pendidikan: str = tingkat_pendidikan

    def get_nama(self) -> str:
        return self._nama

    def get_usia(self) -> int:
        return self._usia

    def get_tingkat_pendidikan(self) -> str:
        return self._tingkat_pendidikan

    def cek_kelayakan(self) -> None:
        if self._usia < 18:
            raise UsiaTidakMemenuhiSyaratError()

        if self._tingkat_pendidikan not in {"Sarjana", "Magister"}:
            raise PendidikanTidakMemenuhiSyaratError()