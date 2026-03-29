class PeralatanOlahraga:
    def __init__(self, jenis: str, merek: str) -> None:
        self._jenis = jenis
        self._merek = merek

    @property
    def jenis(self) -> str:
        return self._jenis

    @property
    def merek(self) -> str:
        return self._merek

    def tampilkan_informasi(self) -> None:
        print(f"Peralatan Olahraga Jenis: {self.jenis}, Merek: {self.merek}")


class Bola(PeralatanOlahraga):
    def __init__(self, jenis: str, merek: str, jenis_olahraga: str, bahan: str) -> None:
        super().__init__(jenis, merek)
        self._jenis_olahraga = jenis_olahraga
        self._bahan = bahan

    @property
    def jenis_olahraga(self) -> str:
        return self._jenis_olahraga

    @property
    def bahan(self) -> str:
        return self._bahan

    def tampilkan_spesifikasi(self) -> None:
        print(f"Jenis Olahraga: {self.jenis_olahraga}, Bahan: {self.bahan}")


class BolaProfesional(Bola):
    def __init__(self, jenis: str, merek: str, jenis_olahraga: str, bahan: str, standar_internasional: bool) -> None:
        super().__init__(jenis, merek, jenis_olahraga, bahan)
        self._standar_internasional = bool(standar_internasional)

    @property
    def standar_internasional(self) -> bool:
        return self._standar_internasional

    def tampilkan_standar(self) -> None:
        status = "Ya" if self.standar_internasional else "Tidak"
        print(
            f"Jenis Olahraga: {self.jenis_olahraga}, Bahan: {self.bahan}, "
            f"Standar Internasional: {status}"
        )


class BolaLatihan(Bola):
    def __init__(self, jenis: str, merek: str, jenis_olahraga: str, bahan: str, harga: int) -> None:
        super().__init__(jenis, merek, jenis_olahraga, bahan)
        self._harga = int(harga)

    @property
    def harga(self) -> int:
        return self._harga


if __name__ == "__main__":
    pro = BolaProfesional(
        jenis="Bola",
        merek="Adidas",
        jenis_olahraga="Sepakbola",
        bahan="Kulit sintetis",
        standar_internasional=True
    )

    latihan = BolaLatihan(
        jenis="Bola",
        merek="Molten",
        jenis_olahraga="Basket",
        bahan="Komposit",
        harga=350000
    )

    pro.tampilkan_informasi()
    pro.tampilkan_spesifikasi()
    pro.tampilkan_standar()

    latihan.tampilkan_informasi()
    latihan.tampilkan_spesifikasi()
    print(f"Harga Bola Latihan: {latihan.harga}")