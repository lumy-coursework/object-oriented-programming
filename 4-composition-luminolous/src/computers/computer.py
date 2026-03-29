from __future__ import annotations

try:
    from .processor import Processor
    from .memory import Memory
except ImportError:
    from processor import Processor
    from memory import Memory

class Computer:
    def __init__(self, processor: Processor, memory: Memory) -> None:
        self._processor: Processor = processor
        self._memory: Memory = memory

    @property
    def processor(self) -> Processor:
        return self._processor

    @processor.setter
    def processor(self, value: Processor) -> None:
        if not isinstance(value, Processor):
            raise TypeError("processor harus bertipe Processor")
        self._processor = value

    @property
    def memory(self) -> Memory:
        return self._memory

    @memory.setter
    def memory(self, value: Memory) -> None:
        if not isinstance(value, Memory):
            raise TypeError("memory harus bertipe Memory")
        self._memory = value

    def get_info(self) -> str:
        return (
            f"Processor Brand: {self._processor.brand}, Kecepatan: {self._processor.speed}, "
            f"Memory Kapasitas: {self._memory.capacity}, Tipe: {self._memory.memory_type}"
        )

if __name__ == "__main__":
    proc = Processor("AMD", 4.0)
    mem = Memory(32, "DDR5")
    pc = Computer(proc, mem)
    print(pc.get_info())

    pc.processor = Processor("Intel", 5.0)
    pc.memory = Memory(64, "DDR5")
    print(pc.get_info())