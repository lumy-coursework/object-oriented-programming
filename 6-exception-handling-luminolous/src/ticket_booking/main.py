from .penumpang import Penumpang
from .pemesanan import PemesananTiket
from .exceptions import (
    KapasitasPenuhError,
    TiketSudahDipesanError,
    NomorTiketTidakDitemukanError,
)


def process_booking(
    pemesanan: PemesananTiket,
    nomor_tiket: str,
    penumpang: Penumpang,
) -> PemesananTiket:
    """
    Memproses pemesanan SATU tiket.

    Unit test mengharapkan:
    - Saat sukses  : mencetak "Pesan tiket berhasil: <nomor_tiket>"
    - Saat kapasitas penuh / duplikat:
        mencetak "Gagal pesan (<nomor_tiket>)" DAN pesan error asli
        (yang mengandung "Kursi sudah penuh" atau "sudah dipesan").
    - SELALU mencetak ringkasan di finally:
        "Jumlah tiket terpesan: X dari Y"
        "Proses pemesanan selesai."
    """
    try:
        try:
            pemesanan.pesan_tiket(nomor_tiket, penumpang)
            print(f"Pesan tiket berhasil: {nomor_tiket}")
        except KapasitasPenuhError as e:
            # sertakan pesan exception supaya ada substring "Kursi sudah penuh"
            print(f"Gagal pesan ({nomor_tiket}): {e}")
        except TiketSudahDipesanError as e:
            # sertakan pesan exception supaya ada substring "sudah dipesan"
            print(f"Gagal pesan ({nomor_tiket}): {e}")
    finally:
        print(
            f"Jumlah tiket terpesan: {pemesanan.get_jumlah_terpesan()} "
            f"dari {pemesanan.get_kapasitas()}"
        )
        print("Proses pemesanan selesai.")

    return pemesanan


def demo() -> None:
    """Demo manual sesuai deskripsi soal."""

    p1 = Penumpang("Andi", "ID001")
    p2 = Penumpang("Budi", "ID002")
    p3 = Penumpang("Citra", "ID003")
    p4 = Penumpang("Dewi", "ID004")

    pesanan = PemesananTiket(2)

    # Sukses
    process_booking(pesanan, "T-001", p1)

    # Kapasitas penuh
    process_booking(pesanan, "T-002", p2)
    process_booking(pesanan, "T-003", p3)

    # Duplikat
    process_booking(pesanan, "T-001", p4)

    try:
        pesanan.batalkan_tiket("XXX")
    except NomorTiketTidakDitemukanError as e:
        print("Gagal membatalkan tiket:", e)


if __name__ == "__main__":
    demo()