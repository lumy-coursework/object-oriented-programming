class Date:
    DEFAULT = (1, 1, 1970)
    def __init__(self, month: int, day: int, year: int) -> None:
        try:
            m = int(month)
            d = int(day)
            y = int(year)
        except (TypeError, ValueError):
            m, d, y = self.DEFAULT

        if not (1 <= m <= 12) or not (1 <= d <= 31):
            m, d, y = self.DEFAULT

        self._month: int = m
        self._day: int = d
        self._year: int = y

    @property
    def month(self) -> int:
        return self._month

    @property
    def day(self) -> int:
        return self._day

    @property
    def year(self) -> int:
        return self._year

    def display_date(self) -> str:
        return f"{self.month:02d}/{self.day:02d}/{self.year:04d}"


if __name__ == "__main__":
    d_ok = Date(9, 21, 2025)
    d_bad = Date(13, 40, 1990)
    print("Valid :", d_ok, ":", d_ok.display_date())
    print("Invalid:", d_bad, ":", d_bad.display_date())