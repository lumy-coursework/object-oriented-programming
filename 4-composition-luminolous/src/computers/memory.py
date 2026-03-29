from __future__ import annotations

class Memory:
    def __init__(self, capacity: int, memory_type: str) -> None:
        self.capacity = capacity
        self.memory_type = memory_type

    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        self._capacity = int(value)

    @property
    def memory_type(self) -> str:
        return self._memory_type

    @memory_type.setter
    def memory_type(self, value: str) -> None:
        self._memory_type = (value or "").strip()

    def __repr__(self) -> str:
        return f"Memory(capacity={self._capacity} GB, type={self._memory_type!r})"

if __name__ == "__main__":
    m = Memory(16, "DDR5")
    print(m)
    m.capacity = 32
    m.memory_type = "DDR4"
    print("Cap:", m.capacity, "GB | Type:", m.memory_type)