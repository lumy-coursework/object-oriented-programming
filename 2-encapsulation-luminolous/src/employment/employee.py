class Employee:
    def __init__(self, first_name: str, last_name: str, monthly_salary: float) -> None:
        self._first_name: str = "Unknown"
        self._last_name: str = "Unknown"
        self._monthly_salary: float = 0.0
        self.first_name = first_name
        self.last_name = last_name
        self.monthly_salary = monthly_salary

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        name = ("" if value is None else str(value)).strip()
        self._first_name = name if name else "Unknown"

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        name = ("" if value is None else str(value)).strip()
        self._last_name = name if name else "Unknown"

    @property
    def monthly_salary(self) -> float:
        return self._monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, value: float) -> None:
        try:
            v = float(value)
        except (TypeError, ValueError):
            return
        if v <= 0:
            return
        self._monthly_salary = v

    def raise_salary(self, raise_percentage: int) -> float:
        try:
            pct = float(raise_percentage)
        except (TypeError, ValueError):
            return self.monthly_salary

        if pct <= 0:
            return self.monthly_salary

        if pct > 20:
            return self.monthly_salary

        self._monthly_salary *= (1.0 + pct / 100.0)
        return self.monthly_salary

    def get_yearly_salary(self) -> float:
        return 12.0 * float(self.monthly_salary)

if __name__ == "__main__":
    e1 = Employee("Budi", "Santoso", 7_000_000)
    e2 = Employee("Ani", "Kusuma", 10_000_000)
    
    print("Gaji Tahunan Sebelum Kenaikan")
    print(e1, "->", e1.get_yearly_salary())
    print(e2, "->", e2.get_yearly_salary())
    
    e1.raise_salary(10)
    e2.raise_salary(10)

    print("\nGaji Tahunan Setelah Kenaikan 10%")
    print(e1, "->", e1.get_yearly_salary())
    print(e2, "->", e2.get_yearly_salary())