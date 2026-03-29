class Invoice:
    def __init__(self, part_number: str, part_description: str, quantity: int, price: float) -> None:
        self._part_number: str = str(part_number)
        self._part_description: str = str(part_description)
        self._quantity: int = 0
        self._price: float = 0.0
        self.quantity = quantity
        self.price = price

    @property
    def part_number(self) -> str:
        return self._part_number

    @part_number.setter
    def part_number(self, value: str) -> None:
        self._part_number = str(value)

    @property
    def part_description(self) -> str:
        return self._part_description

    @part_description.setter
    def part_description(self, value: str) -> None:
        self._part_description = str(value)

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        try:
            v = int(value)
        except (TypeError, ValueError):
            v = 0
        self._quantity = v if v >= 0 else 0

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        try:
            v = float(value)
        except (TypeError, ValueError):
            v = 0.0
        self._price = v if v >= 0 else 0.0

    def get_invoice_amount(self) -> float:
        return float(self.quantity) * float(self.price)

if __name__ == "__main__":
    demo = Invoice("PN-001", "Contoh Barang", 3, 19.99)
    print(demo)
    print(f"Jumlah: {demo.quantity} x {demo.price} = {demo.get_invoice_amount():.2f}")
