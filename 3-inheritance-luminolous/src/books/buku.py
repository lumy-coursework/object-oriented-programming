class Buku:
    def __init__(self, judul: str, pengarang: str) -> None:
        self.judul = judul
        self.pengarang = pengarang

    @property
    def judul(self) -> str:
        return self._judul

    @judul.setter
    def judul(self, value: str) -> None:
        self._judul = str(value).strip()

    @property
    def pengarang(self) -> str:
        return self._pengarang

    @pengarang.setter
    def pengarang(self, value: str) -> None:
        self._pengarang = str(value).strip()

    def tampilkan_info(self) -> None:
        print(f"Buku - Judul: {self.judul}, Pengarang: {self.pengarang}")

class BukuFiksi(Buku):
    def __init__(self, judul: str, pengarang: str, genre: str) -> None:
        super().__init__(judul, pengarang)
        self._genre = genre

    @property
    def genre(self) -> str:
        return self._genre

    @genre.setter
    def genre(self, value: str) -> None:
        self._genre = value

    def tampilkan_info(self) -> None:
        print(
            f"Buku Fiksi - Judul: {self.judul}, Pengarang: {self.pengarang}, "
            f"Genre: {self.genre}"
        )

class BukuPelajaran(Buku):
    def __init__(self, judul: str, pengarang: str, subjek: str) -> None:
        super().__init__(judul, pengarang)
        self._subjek = subjek

    @property
    def subjek(self) -> str:
        return self._subjek

    @subjek.setter
    def subjek(self, value: str) -> None:
        self._subjek = value

    def tampilkan_info(self) -> None:
        print(
            f"Buku Pelajaran - Judul: {self.judul}, Pengarang: {self.pengarang}, "
            f"Subjek: {self.subjek}"
        )

if __name__ == "__main__":
    novel = BukuFiksi(judul="Laut Bercerita", pengarang="Leila S. Chudori", genre="Drama")
    pelajaran = BukuPelajaran(judul="Kalkulus", pengarang="Purcell & Varberg", subjek="Matematika")
    novel.tampilkan_info()
    pelajaran.tampilkan_info()
