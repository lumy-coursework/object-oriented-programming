"""
Buat sistem akun bank sederhana:
- Kelas dasar AkunBank menyimpan pemilik & saldo.
    - Atribut protected: _pemilik: str, _saldo: int
    - Properti GET-only: pemilik, saldo
    - Metode:
        - setoran(jumlah: int): menambah saldo.
        - tarik(jumlah: int): mengurangi saldo.
    - Validasi:
        - jumlah harus > 0
        - Penarikan tidak boleh melebihi saldo (raise ValueError)

- Tabungan (turun dari AkunBank)
    - Atribut tambahan: _bunga_tahunan: float (mis. 0.05 = 5%)
    - Properti GET-only: bunga_tahunan
    - Metode: hitung_bunga_bulanan() -> int (dibulatkan ke bawah)

- Giro (turun dari AkunBank)
    - Atribut tambahan: _biaya_admin: int, _saldo_minimum: int
    - Properti GET-only: biaya_admin, saldo_minimum
    - Metode:
        - potong_biaya_admin(): kurangi saldo dengan biaya admin; jika saldo < saldo_minimum setelah pemotongan, raise ValueError (aturan khusus: giro wajib jaga saldo minimum).
"""

class AkunBank:
    def __init__(self, pemilik: str, saldo_awal: int = 0) -> None:
        if saldo_awal < 0:
            raise ValueError("Saldo awal tidak boleh negatif.")
        self._pemilik = pemilik
        self._saldo = int(saldo_awal)

    @property
    def pemilik(self) -> str:
        return self._pemilik

    @property
    def saldo(self) -> int:
        return self._saldo

    def setoran(self, jumlah: int) -> None:
        if jumlah <= 0:
            raise ValueError("Jumlah setoran harus lebih dari 0.")
        self._saldo += int(jumlah)

    def tarik(self, jumlah: int) -> None:
        if jumlah <= 0:
            raise ValueError("Jumlah penarikan harus lebih dari 0.")
        if jumlah > self._saldo:
            raise ValueError("Saldo tidak mencukupi untuk penarikan.")
        self._saldo -= int(jumlah)


class Tabungan(AkunBank):
    def __init__(self, pemilik: str, saldo_awal: int, bunga_tahunan: float) -> None:
        super().__init__(pemilik, saldo_awal)
        if bunga_tahunan < 0:
            raise ValueError("Bunga tahunan tidak boleh negatif.")
        self._bunga_tahunan = float(bunga_tahunan)

    @property
    def bunga_tahunan(self) -> float:
        return self._bunga_tahunan

    def hitung_bunga_bulanan(self) -> int:
        bunga = self.saldo * (self.bunga_tahunan / 12.0)
        return int(bunga)


class Giro(AkunBank):
    def __init__(self, pemilik: str, saldo_awal: int, biaya_admin: int, saldo_minimum: int) -> None:
        super().__init__(pemilik, saldo_awal)
        if biaya_admin < 0 or saldo_minimum < 0:
            raise ValueError("Biaya admin dan saldo minimum tidak boleh negatif.")
        self._biaya_admin = int(biaya_admin)
        self._saldo_minimum = int(saldo_minimum)

    @property
    def biaya_admin(self) -> int:
        return self._biaya_admin

    @property
    def saldo_minimum(self) -> int:
        return self._saldo_minimum

    def potong_biaya_admin(self) -> None:
        saldo_setelah_potong = self.saldo - self.biaya_admin
        if saldo_setelah_potong < self.saldo_minimum:
            raise ValueError("Pemotongan biaya admin melanggar saldo minimum giro.")
        self._saldo = saldo_setelah_potong


if __name__ == "__main__":
    tabungan = Tabungan(pemilik="Ayu", saldo_awal=5_000_000, bunga_tahunan=0.06)
    print(f"Tabungan {tabungan.pemilik} -> Saldo: {tabungan.saldo}")
    bunga_bulanan = tabungan.hitung_bunga_bulanan()
    print(f"Bunga bulanan (perkiraan): {bunga_bulanan}")
    tabungan.setoran(500_000)
    tabungan.tarik(250_000)
    print(f"Saldo akhir Tabungan: {tabungan.saldo}")

    giro = Giro(pemilik="Bima", saldo_awal=10_000_000, biaya_admin=50_000, saldo_minimum=5_000_000)
    print(f"Giro {giro.pemilik} -> Saldo: {giro.saldo}, Biaya Admin: {giro.biaya_admin}, Saldo Minimum: {giro.saldo_minimum}")
    giro.potong_biaya_admin()
    print(f"Saldo Giro setelah biaya admin: {giro.saldo}")
