from __future__ import annotations

from .penumpang import Penumpang
from .exceptions import (
    KapasitasPenuhError,
    TiketSudahDipesanError,
    NomorTiketTidakDitemukanError,
)


class PemesananTiket:
    def __init__(self, kapasitas: int) -> None:
        # Validasi kapasitas
        if not isinstance(kapasitas, int):
            raise ValueError("Kapasitas harus berupa integer")
        if kapasitas <= 0:
            raise ValueError("Kapasitas harus lebih dari 0")

        self._kapasitas: int = kapasitas
        self._data_tiket: dict[str, Penumpang] = {}

    def pesan_tiket(self, nomor_tiket: str, penumpang: Penumpang) -> None:
        # Validasi nomor tiket
        if not isinstance(nomor_tiket, str) or nomor_tiket.strip() == "":
            raise ValueError("Nomor tiket harus berupa string non-kosong")

        # Cek kapasitas dulu
        if len(self._data_tiket) >= self._kapasitas:
            raise KapasitasPenuhError()

        if nomor_tiket in self._data_tiket:
            raise TiketSudahDipesanError()

        self._data_tiket[nomor_tiket] = penumpang

    def batalkan_tiket(self, nomor_tiket: str) -> None:
        if nomor_tiket not in self._data_tiket:
            raise NomorTiketTidakDitemukanError()

        del self._data_tiket[nomor_tiket]

    def ada_tiket(self, nomor_tiket: str) -> bool:
        """Helper untuk unit test: mengecek apakah nomor_tiket terdaftar."""
        return nomor_tiket in self._data_tiket

    def get_jumlah_terpesan(self) -> int:
        return len(self._data_tiket)

    def get_kapasitas(self) -> int:
        return self._kapasitas