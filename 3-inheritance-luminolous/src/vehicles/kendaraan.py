class Kendaraan:
    def __init__(self, merk: str, model: str) -> None:
        self._merk = merk
        self._model = model

    @property
    def merk(self) -> str:
        return self._merk

    @property
    def model(self) -> str:
        return self._model

    def tampilkan_info(self) -> None:
        print(f"Kendaraan - Merk: {self.merk}, Model: {self.model}")


class Mobil(Kendaraan):
    def __init__(self, merk: str, model: str, tipe_bodi: str) -> None:
        super().__init__(merk, model)
        self._tipe_bodi = tipe_bodi

    @property
    def tipe_bodi(self) -> str:
        return self._tipe_bodi

    def tampilkan_info(self) -> None:
        print(
            f"Mobil - Merk: {self.merk}, Model: {self.model}, "
            f"Tipe Bodi: {self.tipe_bodi}"
        )


class Motor(Kendaraan):
    def __init__(self, merk: str, model: str, tipe_mesin: str) -> None:
        super().__init__(merk, model)
        self._tipe_mesin = tipe_mesin

    @property
    def tipe_mesin(self) -> str:
        return self._tipe_mesin

    def tampilkan_info(self) -> None:
        print(
            f"Motor - Merk: {self.merk}, Model: {self.model}, "
            f"Tipe Mesin: {self.tipe_mesin}"
        )


if __name__ == "__main__":
    mobil = Mobil(merk="Toyota", model="Avanza", tipe_bodi="Sedan")
    motor = Motor(merk="Honda", model="CBR150R", tipe_mesin="4 Stroke")
    mobil.tampilkan_info()
    motor.tampilkan_info()