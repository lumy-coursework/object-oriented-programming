class Buku():
    def __init__(self, judul: str, penulis: str, tahun_terbit: int) -> None:
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
    
    def tampilkan_info(self) -> str:
        print(f"Judul: {self.judul}, Penulis: {self.penulis}, Tahun Terbit: {self.tahun_terbit}")
    
if __name__ == "__main__":
    buku = Buku("The Fragrant Flower Blooms with Dignity", "Saka Mikami", 2021)
    buku.tampilkan_info()