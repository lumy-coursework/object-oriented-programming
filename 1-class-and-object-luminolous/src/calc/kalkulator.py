class Kalkulator():
    def tambah(self, a: float, b:float) -> float:
        return a + b
    
    def kurang(self, a: float, b:float) -> float:
        return a - b

    def kali(self, a: float, b:float) -> float:
        return a * b
    
    def bagi(self, a: float, b:float) -> float:
        try:
            return a / b
        except ZeroDivisionError as e:
            raise e
            

if __name__ == "__main__":
    a, b = map(int, input("Masukkan nilai a dan b: ").split())
    op = input("Masukkan jenis operasi(+, -, *, /): ")
    kalkulator = Kalkulator()
    if op == "+":
        print(kalkulator.tambah(a, b))

    elif op == "-":
        print(kalkulator.kurang(a, b))

    elif op == "*":
        print(kalkulator.kali(a, b))

    elif op == "/":
        print(kalkulator.bagi(a, b))
