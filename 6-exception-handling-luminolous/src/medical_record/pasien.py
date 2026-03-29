from __future__ import annotations

from .exceptions import DataTidakLengkapError, DataTidakValidError


class Pasien:
    def __init__(self, nama: str, umur: int, alamat: str) -> None:
        self._nama: str = nama
        self._umur: int = umur
        self._alamat: str = alamat

    def get_nama(self) -> str:
        return self._nama

    def validasi_data(self) -> None:
        if self._nama.strip() == "" or self._alamat.strip() == "":
            raise DataTidakLengkapError()

        if self._umur < 0 or self._umur > 120:
            raise DataTidakValidError()