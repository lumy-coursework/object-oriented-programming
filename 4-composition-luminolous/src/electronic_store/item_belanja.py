from __future__ import annotations

try:
    from .produk import Produk
except ImportError:
    from produk import Produk

class ItemBelanja:
    def __init__(self, produk: Produk, kuantitas: int) -> None:
        self.produk = produk
        self._kuantitas: int = 0
        self.kuantitas = kuantitas

    @property
    def produk(self) -> Produk:
        return self._produk

    @produk.setter
    def produk(self, value: Produk) -> None:
        if not isinstance(value, Produk):
            raise TypeError("produk harus bertipe Produk")
        self._produk = value

    @property
    def kuantitas(self) -> int:
        return self._kuantitas

    @kuantitas.setter
    def kuantitas(self, value: int) -> None:
        v = int(value)
        self._kuantitas = v if v >= 0 else 0

    def hitung_total(self) -> float:
        return self._produk.harga * self._kuantitas

    def __repr__(self) -> str:
        return f"ItemBelanja({self._produk!r}, qty={self._kuantitas})"

if __name__ == "__main__":
    it = ItemBelanja(Produk("Mouse", 150_000), 2)
    print(it, "| Total:", it.hitung_total())
    it.kuantitas = -3
    print(it, "| Total:", it.hitung_total())