class DataTidakLengkapError(Exception):
    def __init__(self, message: str = "Data pasien tidak lengkap."):
        super().__init__(message)


class DataTidakValidError(Exception):
    def __init__(self, message: str = "Data yang dimasukkan tidak valid."):
        super().__init__(message)