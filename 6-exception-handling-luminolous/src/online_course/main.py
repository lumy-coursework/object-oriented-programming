from .kursus import KursusOnline
from .peserta import Peserta
from .exceptions import (
    UsiaTidakMemenuhiSyaratError,
    PendidikanTidakMemenuhiSyaratError,
)


def process_registration(kursus: KursusOnline, peserta: Peserta) -> KursusOnline:
    """
    Memproses pendaftaran SATU peserta ke dalam KursusOnline.

    Unit test mengharapkan:
    - Saat sukses  : mencetak "Pendaftaran berhasil: <nama>"
    - Saat gagal   : mencetak "Gagal daftar (<nama>)" DAN pesan error asli
      (mis. mengandung "usia Anda tidak memenuhi syarat" atau
      "tingkat pendidikan Anda tidak memenuhi syarat").
    - SELALU mencetak "Proses pendaftaran selesai." di blok finally.
    """
    try:
        kursus.daftar_peserta(peserta)
        print(f"Pendaftaran berhasil: {peserta.get_nama()}")
    except UsiaTidakMemenuhiSyaratError as e:
        # sekarang juga menampilkan pesan error asli
        print(f"Gagal daftar ({peserta.get_nama()}): {e}")
    except PendidikanTidakMemenuhiSyaratError as e:
        print(f"Gagal daftar ({peserta.get_nama()}): {e}")
    finally:
        print("Proses pendaftaran selesai.")

    return kursus


def demo() -> None:
    """Demo manual (tidak dipakai di unit test)."""
    kursus = KursusOnline()

    calon_peserta = [
        Peserta("Andi", 17, "SMA"),
        Peserta("Budi", 22, "Sarjana"),
        Peserta("Citra", 25, "Diploma"),
        Peserta("Dewi", 30, "Magister"),
    ]

    for p in calon_peserta:
        process_registration(kursus, p)

    print("\n=== Peserta yang berhasil terdaftar ===")
    for p in kursus.get_daftar_peserta():
        print("-", p.get_nama())


if __name__ == "__main__":
    demo()