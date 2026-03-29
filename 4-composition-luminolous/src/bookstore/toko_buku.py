from __future__ import annotations

try:
    from .buku import Buku
except ImportError:
    from buku import Buku

class TokoBuku:
    def __init__(self) -> None:
        self._daftar_buku: list[Buku] = []

    @property
    def daftar_buku(self):
        raise AttributeError("Gunakan metode get_daftar_buku() untuk melihat daftar, atau setter untuk mengganti.")

    @daftar_buku.setter
    def daftar_buku(self, value: list[Buku]) -> None:
        if not isinstance(value, list) or not all(isinstance(x, Buku) for x in value):
            raise TypeError("daftar_buku harus berupa list[Buku].")
        self._daftar_buku = value

    def tambah_buku(self, buku: Buku) -> None:
        if not isinstance(buku, Buku):
            raise TypeError("Argumen harus bertipe Buku.")
        self._daftar_buku.append(buku)

    def hapus_buku(self, isbn: str) -> None:
        for i, b in enumerate(self._daftar_buku):
            if b.is_isbn_match(isbn):
                del self._daftar_buku[i]
                return

    def cari_buku(self, isbn: str) -> Buku | None:
        return next((b for b in self._daftar_buku if b.is_isbn_match(isbn)), None)

    def get_daftar_buku(self) -> list[str]:
        return [b.get_info() for b in self._daftar_buku]

if __name__ == "__main__":
    toko = TokoBuku()
    toko.tambah_buku(Buku("978-623-1111-11-1", "Algoritma & Struktur Data", 99000))
    toko.tambah_buku(Buku("978-623-2222-22-2", "Machine Learning Dasar", 149000))
    toko.tambah_buku(Buku("978-623-3333-33-3", "Sistem Operasi", 120000))

    print("Daftar awal:")
    for info in toko.get_daftar_buku():
        print("-", info)

    print("\nCari buku 2222-22-2:", toko.cari_buku("978-623-2222-22-2"))

    print("\nHapus satu buku")
    toko.hapus_buku("978-623-1111-11-1")
    for info in toko.get_daftar_buku():
        print("-", info)

    print("\nGanti daftar sekaligus (setter-only property):")
    toko.daftar_buku = [Buku("X-1", "Buku Dummy 1", 10000), Buku("X-2", "Buku Dummy 2", 20000)]
    for info in toko.get_daftar_buku():
        print("-", info)