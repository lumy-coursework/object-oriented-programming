# src/extra/extra.py

class NilaiTidakValidError(Exception):
    def __init__(self, message: str = "Nilai harus antara 0 dan 100."):
        super().__init__(message)


class PerhitunganRataRataError(Exception):
    def __init__(
        self,
        message: str = "Gagal menghitung rata-rata nilai.",
    ):
        super().__init__(message)


def validasi_nilai(nilai_list: list[float]) -> None:
    """Memvalidasi bahwa semua nilai berada di antara 0 dan 100."""
    for n in nilai_list:
        if n < 0 or n > 100:
            raise NilaiTidakValidError(
                f"Nilai {n} berada di luar rentang 0–100."
            )


def hitung_rata_rata(nilai_list: list[float]) -> float:
    """Menghitung rata-rata dengan exception chaining."""
    try:
        validasi_nilai(nilai_list)
    except NilaiTidakValidError as e:
        # chaining: perhitungan rata-rata gagal karena nilai tidak valid
        raise PerhitunganRataRataError(
            "Tidak dapat menghitung rata-rata karena terdapat nilai tidak valid."
        ) from e

    if not nilai_list:
        # contoh alur tidak normal lain
        raise PerhitunganRataRataError("Daftar nilai kosong.")

    return sum(nilai_list) / len(nilai_list)


def demo_skenario() -> None:
    skenario = {
        "nilai_valid": [80, 90, 75],
        "nilai_dengan_salah": [100, 120, 90],  # 120 tidak valid
        "nilai_kosong": [],
    }

    # 1. Skenario nilai valid
    print("=== Skenario 1: Nilai Valid ===")
    try:
        rata = hitung_rata_rata(skenario["nilai_valid"])
        print("Rata-rata:", rata)
    except (NilaiTidakValidError, PerhitunganRataRataError) as e:
        print("Error:", e)
        if e.__cause__:
            print("Penyebab asli:", e.__cause__)
    finally:
        print("Blok finally tetap dijalankan (skenario 1).\n")

    # 2. Skenario nilai tidak valid
    print("=== Skenario 2: Ada Nilai Tidak Valid ===")
    try:
        rata = hitung_rata_rata(skenario["nilai_dengan_salah"])
        print("Rata-rata:", rata)
    except PerhitunganRataRataError as e:
        print("Error:", e)
        print("Penyebab asli:", e.__cause__)
    finally:
        print("Blok finally tetap dijalankan (skenario 2).\n")

    # 3. Skenario daftar nilai kosong
    print("=== Skenario 3: Daftar Nilai Kosong ===")
    try:
        rata = hitung_rata_rata(skenario["nilai_kosong"])
        print("Rata-rata:", rata)
    except PerhitunganRataRataError as e:
        print("Error:", e)
    finally:
        print("Blok finally tetap dijalankan (skenario 3).\n")

    print("Program tetap berakhir normal meskipun terjadi beberapa error.")


if __name__ == "__main__":
    demo_skenario()
