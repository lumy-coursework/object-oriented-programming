from __future__ import annotations
from abc import ABC, abstractmethod

class Hewan(ABC):
    def __init__(self, nama: str) -> None:
        self._nama = ""
        self.nama = nama  # validasi via setter

    @property
    def nama(self) -> str:
        return self._nama

    @nama.setter
    def nama(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("nama harus berupa string")
        cleaned = value.strip()
        if cleaned == "":
            raise ValueError("nama tidak boleh kosong")
        self._nama = cleaned

    @abstractmethod
    def bersuara(self) -> str:
        raise NotImplementedError


class Kucing(Hewan):
    def bersuara(self) -> str:
        return "Meong"


class Anjing(Hewan):
    def bersuara(self) -> str:
        return "Guk"