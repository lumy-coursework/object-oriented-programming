from .pasien import Pasien
from .pemeriksaan import Pemeriksaan
from .exceptions import DataTidakLengkapError, DataTidakValidError


def demo() -> None:
    pemeriksa = Pemeriksaan()

    pasien_list = [
        Pasien("Andi", 25, "Jl. Merdeka"),
        Pasien("", 30, "Jl. Sudirman"),          # nama kosong
        Pasien("Budi", 200, "Jl. Mawar"),        # umur tidak valid
        Pasien("Citra", 40, ""),                 # alamat kosong
    ]

    for p in pasien_list:
        print(f"\nMemeriksa data pasien: {p.get_nama()!r}")
        try:
            hasil = pemeriksa.periksa_data(p)
            print("Hasil:", hasil)
        except DataTidakLengkapError as e:
            print("Error (lengkap):", e)
            print("Pesan asli   :", e.__cause__)
        except DataTidakValidError as e:
            print("Error (valid):", e)
            print("Pesan asli   :", e.__cause__)


if __name__ == "__main__":
    demo()