from __future__ import annotations


class Penumpang:
    def __init__(self, nama: str, nomor_identitas: str) -> None:
        # Validasi nama
        if not isinstance(nama, str) or nama.strip() == "":
            raise ValueError("Nama penumpang harus berupa string non-kosong")

        # Validasi nomor identitas
        if not isinstance(nomor_identitas, str) or nomor_identitas.strip() == "":
            raise ValueError("Nomor identitas harus berupa string non-kosong")

        self._nama: str = nama
        self._nomor_identitas: str = nomor_identitas

    def get_identitas(self) -> str:
        return self._nomor_identitas

    def get_nama(self) -> str:
        return self._nama