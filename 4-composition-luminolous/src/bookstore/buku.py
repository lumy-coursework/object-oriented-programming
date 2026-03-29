from __future__ import annotations
import re

def _norm_isbn(s: str) -> str:
    return re.sub(r"[^0-9A-Za-z]+", "", (s or "").strip()).upper()

class Buku:
    def __init__(self, isbn: str, judul: str, harga: float) -> None:
        self._isbn: str = (isbn or "").strip()
        self._judul: str = (judul or "").strip()
        self._harga: float = float(harga)

    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def judul(self) -> str:
        return self._judul

    @property
    def harga(self) -> float:
        return self._harga

    def is_isbn_match(self, isbn: str) -> bool:
        return _norm_isbn(self._isbn) == _norm_isbn(isbn)

    def get_info(self) -> str:
        return f"ISBN: {self._isbn}, Judul: {self._judul}, Harga: {self._harga:.1f}"

    def __repr__(self) -> str:
        return f"Buku(isbn={self._isbn!r}, judul={self._judul!r}, harga={self._harga})"

if __name__ == "__main__":
    b = Buku("978-602-1234-56-7", "Pemrograman Python Dasar", 125000)
    print(b.get_info())
    print("ISBN match?", b.is_isbn_match("978-602-1234-56-7"))