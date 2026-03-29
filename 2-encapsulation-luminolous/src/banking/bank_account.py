class BankAccount:
    def __init__(self, account_number: str, account_holder: str, balance: float = 0.0) -> None:
        num = ("" if account_number is None else str(account_number)).strip()
        holder = ("" if account_holder is None else str(account_holder)).strip()
        self._account_number: str = num if num else "Unknown"
        self._account_holder: str = holder if holder else "Unknown"

        try:
            bal = float(balance)
        except (TypeError, ValueError):
            bal = 0.0
        self._balance: float = bal if bal >= 0 else 0.0

    @property
    def account_number(self) -> str:
        return self._account_number

    @property
    def account_holder(self) -> str:
        return self._account_holder

    def deposit(self, amount: float) -> float:
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            return self._balance
        if amt < 0:
            return self._balance
        self._balance += amt
        return self._balance

    def withdraw(self, amount: float) -> float:
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            return self._balance
        if amt < 0:
            return self._balance
        if amt <= self._balance:
            self._balance -= amt
        return self._balance

    def get_balance(self) -> float:
        return self._balance

    def __repr__(self) -> str:
        return (f"BankAccount(account_number={self._account_number!r}, "
                f"account_holder={self._account_holder!r}, "
                f"balance={self._balance})")


if __name__ == "__main__":
    acct = BankAccount("", "Budi Santoso", -1000)
    print("Akun awal:", acct)

    print("\nSetoran 2.500.000")
    acct.deposit(2_500_000)
    print("Saldo:", acct.get_balance())

    print("\nTarik 500.000")
    acct.withdraw(500_000)
    print("Saldo:", acct.get_balance())

    print("\nCoba tarik 3.000.000 (lebih dari saldo) -> diabaikan")
    acct.withdraw(3_000_000)
    print("Saldo akhir:", acct.get_balance())