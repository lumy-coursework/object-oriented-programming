class Sepeda():
    def __init__(self, merk: str, tipe: str, berat: int) -> None:
        self.merk = merk
        self.tipe = tipe
        self.berat = berat
    
    def tampilkan_informasi(self) -> str:
        print(f"Merek: {self.merk}, Tipe: {self.tipe}, Berat: {self.berat} kg")
    
if __name__ == "__main__":
    sepeda = Sepeda("polygon", "chiyo", 14.5)
    sepeda.tampilkan_informasi()