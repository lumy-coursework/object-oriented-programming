class Mobil():
    def __init__(self, merk: str, model: str, tahun_produksi: int) -> None:
        self.merk = merk
        self.model = model
        self.tahun_produksi = tahun_produksi
    
    def tampilkan_spesifikasi(self) -> str:
        print(f"Merk: {self.merk}, Model: {self.model}, Tahun Produksi: {self.tahun_produksi}")
    
if __name__ == "__main__":
    mobil = Mobil("Bugatti", "Chiron", 2015)
    mobil.tampilkan_spesifikasi()