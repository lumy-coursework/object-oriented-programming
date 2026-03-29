from __future__ import annotations

from .pasien import Pasien
from .exceptions import DataTidakLengkapError, DataTidakValidError


class Pemeriksaan:
    def periksa_data(self, pasien: Pasien) -> str:
        try:
            pasien.validasi_data()
        except DataTidakLengkapError as e:
            # chaining: memperkaya pesan error
            raise DataTidakLengkapError(
                "Validasi gagal: nama/alamat kosong."
            ) from e
        except DataTidakValidError as e:
            # Perhatikan pesan harus sama dengan yang diharapkan test
            raise DataTidakValidError(
                "Validasi gagal: umur di luar rentang 0–120."
            ) from e

        return "Data pasien valid"