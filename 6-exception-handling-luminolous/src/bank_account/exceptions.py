class SaldoTidakCukupError(Exception):
    def __init__(self, message: str = "Saldo tidak mencukupi!"):
        super().__init__(message)


class RekeningTidakDitemukanError(Exception):
    def __init__(self, message: str = "Rekening tidak ditemukan!"):
        super().__init__(message)


class BatasPenarikanError(Exception):
    def __init__(self, message: str = "Melebihi batas penarikan harian."):
        super().__init__(message)