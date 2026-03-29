from __future__ import annotations

from .rekening import Rekening
from .exceptions import RekeningTidakDitemukanError


class Bank:
    def __init__(self) -> None:
        self._daftar: dict[str, Rekening] = {}

    def tambah_rekening(self, rek: Rekening) -> None:
        nomor = rek.get_nomor()
        if nomor in self._daftar:
            raise ValueError("Nomor rekening sudah ada")
        self._daftar[nomor] = rek

    def cari_rekening(self, nomor: str) -> Rekening:
        try:
            return self._daftar[nomor]
        except KeyError as e:
            # bisa pakai chaining untuk memperkaya konteks
            raise RekeningTidakDitemukanError() from e

    def get_semua_rekening(self) -> list[Rekening]:
        """Metode bantu untuk demo/printing saldo."""
        return list(self._daftar.values())