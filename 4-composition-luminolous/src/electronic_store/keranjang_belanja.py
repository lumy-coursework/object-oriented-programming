from __future__ import annotations

try:
    from .produk import Produk
    from .item_belanja import ItemBelanja
except ImportError:
    from produk import Produk
    from item_belanja import ItemBelanja

class KeranjangBelanja:
    def __init__(self) -> None:
        self._items: list[ItemBelanja] = []

    @property
    def items(self) -> list[ItemBelanja]:
        return self._items

    def tambah_item_belanja(self, produk: Produk, kuantitas: int) -> None:
        if not isinstance(produk, Produk):
            raise TypeError("produk harus bertipe Produk")
        item = ItemBelanja(produk, kuantitas)
        self._items.append(item)

    def hitung_total_belanja(self) -> float:
        return sum(item.hitung_total() for item in self._items)

    def __repr__(self) -> str:
        return f"KeranjangBelanja(items={self._items!r})"

if __name__ == "__main__":
    keranjang = KeranjangBelanja()
    keranjang.tambah_item_belanja(Produk("Laptop", 12_500_000), 1)
    keranjang.tambah_item_belanja(Produk("SSD 1TB", 1_500_000), 2)
    keranjang.tambah_item_belanja(Produk("USB-C Hub", 350_000), 3)

    print("Item di keranjang:")
    for it in keranjang.items:
        print("-", it, "| subtotal:", it.hitung_total())

    print("TOTAL BELANJA:", keranjang.hitung_total_belanja())