class UsiaTidakMemenuhiSyaratError(Exception):
    def __init__(
        self,
        message: str = "Maaf, usia Anda tidak memenuhi syarat untuk mengikuti kursus ini.",
    ):
        super().__init__(message)


class PendidikanTidakMemenuhiSyaratError(Exception):
    def __init__(
        self,
        message: str = (
            "Maaf, tingkat pendidikan Anda tidak memenuhi syarat untuk mengikuti kursus ini."
        ),
    ):
        super().__init__(message)