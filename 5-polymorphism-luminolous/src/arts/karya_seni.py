from __future__ import annotations
from abc import ABC, abstractmethod

class KaryaSeni(ABC):
    def __init__(self, judul: str) -> None:
        self._judul = ""
        self.judul = judul  # validasi via setter

    @property
    def judul(self) -> str:
        return self._judul

    @judul.setter
    def judul(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("judul harus berupa string")
        cleaned = value.strip()
        if cleaned == "":
            raise ValueError("judul tidak boleh kosong")
        self._judul = cleaned

    @abstractmethod
    def deskripsi(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def tampilkan(self) -> str:
        raise NotImplementedError


class Lukisan(KaryaSeni):
    def deskripsi(self) -> str:
        return "Sebuah gambar yang dilukis di atas kanvas"

    def tampilkan(self) -> str:
        return "Digantung di dinding"


class Patung(KaryaSeni):
    def deskripsi(self) -> str:
        return "Sebuah objek tiga dimensi yang dibentuk"

    def tampilkan(self) -> str:
        return "Diletakkan di atas meja atau lantai"