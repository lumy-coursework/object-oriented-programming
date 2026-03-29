from __future__ import annotations

from .peserta import Peserta


class KursusOnline:
    def __init__(self) -> None:
        self._peserta: list[Peserta] = []

    def daftar_peserta(self, peserta: Peserta) -> None:
        # akan raise exception jika tidak layak
        peserta.cek_kelayakan()
        self._peserta.append(peserta)

    def get_daftar_peserta(self) -> list[Peserta]:
        # copy supaya list internal tidak bisa dimodifikasi dari luar
        return list(self._peserta)