class KapasitasPenuhError(Exception):
    def __init__(
        self,
        message: str = "Kursi sudah penuh, tidak dapat memproses pemesanan.",
    ):
        super().__init__(message)


class TiketSudahDipesanError(Exception):
    def __init__(
        self,
        message: str = "Tiket untuk penumpang ini sudah dipesan.",
    ):
        super().__init__(message)


class NomorTiketTidakDitemukanError(Exception):
    def __init__(
        self,
        message: str = "Nomor tiket tidak ditemukan dalam sistem.",
    ):
        super().__init__(message)