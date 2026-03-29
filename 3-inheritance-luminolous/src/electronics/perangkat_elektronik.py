class PerangkatElektronik:
    def __init__(self, brand: str, model: str) -> None:
        self._brand = brand
        self._model = model

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def model(self) -> str:
        return self._model

    def tampilkan_identitas(self) -> None:
        print(f"Perangkat Brand: {self.brand}, Model: {self.model}")


class Smartphone(PerangkatElektronik):
    def __init__(self, brand: str, model: str, sistem_operasi: str, fitur_dasar: str) -> None:
        super().__init__(brand, model)
        self._sistem_operasi = sistem_operasi
        self._fitur_dasar = fitur_dasar

    @property
    def sistem_operasi(self) -> str:
        return self._sistem_operasi

    @property
    def fitur_dasar(self) -> str:
        return self._fitur_dasar

    def tampilkan_fitur_dasar(self) -> None:
        print(f"Fitur Dasar: {self.fitur_dasar}")


class FlagshipPhone(Smartphone):
    def __init__(self, brand: str, model: str, sistem_operasi: str, fitur_dasar: str, fitur_premium: str) -> None:
        super().__init__(brand, model, sistem_operasi, fitur_dasar)
        self._fitur_premium = fitur_premium

    @property
    def fitur_premium(self) -> str:
        return self._fitur_premium

    def tampilkan_fitur_premium(self) -> None:
        self.tampilkan_fitur_dasar()
        print(f"Fitur Premium: {self.fitur_premium}")


class BudgetPhone(Smartphone):
    def __init__(self, brand: str, model: str, sistem_operasi: str, fitur_dasar: str, harga: int) -> None:
        super().__init__(brand, model, sistem_operasi, fitur_dasar)
        self._harga = int(harga)

    @property
    def harga(self) -> int:
        return self._harga


if __name__ == "__main__":
    flagship = FlagshipPhone(
        brand="Galaxy",
        model="S25 Ultra",
        sistem_operasi="Android",
        fitur_dasar="Layar AMOLED & Kamera Multi",
        fitur_premium="Zoom periskop 10x & AI fotografi"
    )

    murah = BudgetPhone(
        brand="Redmi",
        model="A4",
        sistem_operasi="Android",
        fitur_dasar="Dual SIM & Baterai besar",
        harga=1499000
    )

    flagship.tampilkan_identitas()
    flagship.tampilkan_fitur_dasar()
    flagship.tampilkan_fitur_premium()

    murah.tampilkan_identitas()
    murah.tampilkan_fitur_dasar()
    print(f"Harga BudgetPhone: {murah.harga}")