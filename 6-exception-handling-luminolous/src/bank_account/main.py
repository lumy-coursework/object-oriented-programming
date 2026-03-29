from .bank import Bank
from .rekening import Rekening
from .exceptions import (
    SaldoTidakCukupError,
    BatasPenarikanError,
    RekeningTidakDitemukanError,
)


def demo() -> None:
    bank = Bank()

    # Tambah beberapa rekening
    r1 = Rekening("001", saldo_awal=200_000)
    r2 = Rekening("002", saldo_awal=50_000)
    r3 = Rekening("003", saldo_awal=150_000)

    bank.tambah_rekening(r1)
    bank.tambah_rekening(r2)
    bank.tambah_rekening(r3)

    try:
        # Penarikan valid
        bank.cari_rekening("001").penarikan(50_000)

        # Penarikan melebihi batas harian
        bank.cari_rekening("002").penarikan(150_000)

        # Penarikan melebihi saldo
        bank.cari_rekening("003").penarikan(200_000)

        # Mencoba rekening yang tidak ada
        bank.cari_rekening("999").penarikan(10_000)

    except SaldoTidakCukupError as e:
        print("Terjadi SaldoTidakCukupError:", e)
    except BatasPenarikanError as e:
        print("Terjadi BatasPenarikanError:", e)
    except RekeningTidakDitemukanError as e:
        print("Terjadi RekeningTidakDitemukanError:", e)
    except Exception as e:
        # Fallback logging
        print("Terjadi error tak terduga:", e)
    finally:
        print("\n=== Saldo Akhir Rekening ===")
        for rek in bank.get_semua_rekening():
            print(f"Rekening {rek.get_nomor()}: {rek.get_saldo()}")


if __name__ == "__main__":
    demo()