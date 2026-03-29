from __future__ import annotations

class Produk:
    def __init__(self, nama: str, harga: float) -> None:
        self.nama = nama
        self.harga = harga

    @property
    def nama(self) -> str:
        return self._nama

    @nama.setter
    def nama(self, value: str) -> None:
        self._nama = (value or "").strip()

    @property
    def harga(self) -> float:
        return self._harga

    @harga.setter
    def harga(self, value: float) -> None:
        self._harga = float(value)

    def __repr__(self) -> str:
        return f"Produk(nama={self._nama!r}, harga={self._harga})"

if __name__ == "__main__":
    p = Produk("Headset", 250_000)
    print(p)
    p.harga = 225_000
    print("Nama:", p.nama, "| Harga:", p.harga)