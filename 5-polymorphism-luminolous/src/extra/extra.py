"""
Intinya:
- Pembayaran adalah abstract class (punya jumlah dan metode abstrak proses()).
- TransferBank dan EWallet mewarisi Pembayaran.
- PemrosesPembayaran menampung banyak pembayaran dan memproses semuanya secara polymorphic 
  (tanpa peduli tipenya, asal turunan Pembayaran).
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Pembayaran(ABC):
    """
    Kelas abstrak yang mewakili suatu metode pembayaran.
    Tiap pembayaran punya jumlah (float, >0) dan bisa diproses.
    """

    def __init__(self, jumlah: float) -> None:
        self._jumlah = 0.0
        self.jumlah = jumlah

    @property
    def jumlah(self) -> float:
        return self._jumlah

    @jumlah.setter
    def jumlah(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("jumlah harus numerik")
        if value <= 0:
            raise ValueError("jumlah harus > 0")
        self._jumlah = float(value)

    @abstractmethod
    def proses(self) -> str:
        """
        Mengembalikan string hasil proses pembayaran.
        """
        raise NotImplementedError


class TransferBank(Pembayaran):
    def __init__(self, jumlah: float, norek_tujuan: str) -> None:
        super().__init__(jumlah)
        self._norek_tujuan = ""
        self.norek_tujuan = norek_tujuan

    @property
    def norek_tujuan(self) -> str:
        return self._norek_tujuan

    @norek_tujuan.setter
    def norek_tujuan(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("norek_tujuan harus string")
        if value.strip() == "":
            raise ValueError("norek_tujuan tidak boleh kosong")
        self._norek_tujuan = value

    def proses(self) -> str:
        return (
            f"Transfer Bank sebesar {self.jumlah:.2f} "
            f"ke rekening {self.norek_tujuan} berhasil."
        )


class EWallet(Pembayaran):
    def __init__(self, jumlah: float, akun: str) -> None:
        super().__init__(jumlah)
        self._akun = ""
        self.akun = akun

    @property
    def akun(self) -> str:
        return self._akun

    @akun.setter
    def akun(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("akun harus string")
        if value.strip() == "":
            raise ValueError("akun tidak boleh kosong")
        self._akun = value

    def proses(self) -> str:
        return (
            f"Pembayaran E-Wallet sebesar {self.jumlah:.2f} "
            f"melalui akun {self.akun} berhasil."
        )


class PemrosesPembayaran:
    """
    Kelas utilitas yang menyimpan daftar pembayaran (polymorphism).
    Kita hanya peduli bahwa tiap objek punya .proses().
    """

    def __init__(self) -> None:
        self._daftar: List[Pembayaran] = []

    def tambah_pembayaran(self, bayar: Pembayaran) -> None:
        if not isinstance(bayar, Pembayaran):
            raise TypeError("Parameter harus turunan Pembayaran")
        self._daftar.append(bayar)

    def proses_semua(self) -> list[str]:
        hasil: list[str] = []
        for b in self._daftar:
            hasil.append(b.proses())  # polymorphism di sini
        return hasil


if __name__ == "__main__":
    p1 = TransferBank(150000, "1234567890")
    p2 = EWallet(50000, "user@example")

    kasir = PemrosesPembayaran()
    kasir.tambah_pembayaran(p1)
    kasir.tambah_pembayaran(p2)

    for line in kasir.proses_semua():
        print(line)