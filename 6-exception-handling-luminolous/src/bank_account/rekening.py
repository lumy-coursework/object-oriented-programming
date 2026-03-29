from __future__ import annotations

from .exceptions import SaldoTidakCukupError, BatasPenarikanError


class Rekening:
    BATAS_PENARIKAN_HARIAN = 100_000  # misal rupiah

    def __init__(self, nomor: str, saldo_awal: float = 0.0) -> None:
        # Validasi nomor rekening
        if not isinstance(nomor, str) or nomor.strip() == "":
            raise ValueError("Nomor rekening harus berupa string non-kosong")

        # Validasi saldo awal
        if not isinstance(saldo_awal, (int, float)):
            raise ValueError("Saldo awal harus berupa angka")
        if saldo_awal < 0:
            raise ValueError("Saldo awal tidak boleh negatif")

        self._nomor: str = nomor
        self._saldo: float = float(saldo_awal)

    def penarikan(self, jumlah: float) -> None:
        """Melakukan penarikan saldo dengan berbagai validasi."""
        # Tangani jika jumlah bukan angka -> ValueError (bukan TypeError)
        if not isinstance(jumlah, (int, float)):
            raise ValueError("Jumlah penarikan harus berupa angka")

        if jumlah <= 0:
            raise ValueError("Jumlah penarikan harus > 0")

        if jumlah > self.BATAS_PENARIKAN_HARIAN:
            raise BatasPenarikanError()

        if jumlah > self._saldo:
            raise SaldoTidakCukupError()

        self._saldo -= jumlah

    def get_saldo(self) -> float:
        return self._saldo

    def get_nomor(self) -> str:
        return self._nomor