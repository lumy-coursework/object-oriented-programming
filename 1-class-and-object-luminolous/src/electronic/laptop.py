class Laptop():
    def __init__(self, merk: str, prosesor: str, ram: int, penyimpanan: int) -> None:
        self.merk = merk
        self.prosesor = prosesor
        self.ram = ram
        self.penyimpanan = penyimpanan
    
    def tampilkan_spesifikasi(self) -> str:
        print(f"Merk: {self.merk}, Prosesor: {self.prosesor}, RAM: {self.ram} GB, Penyimpanan: {self.penyimpanan} GB")
    
if __name__ == "__main__":
    laptop = Laptop("Lenovo", "Intel", 12, 512)
    laptop.tampilkan_spesifikasi()