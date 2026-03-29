from __future__ import annotations
from typing import Any, List
from .email_sender import EmailSender
from .sms_sender import SmsSender
from .push_sender import PushSender
from .broken_sender import BrokenSender

class Notifier:
    def __init__(self) -> None:
        self._pengirim: List[Any] = []

    def tambah_pengirim(self, pengirim: Any) -> None:
        self._pengirim.append(pengirim)

    def kirim(self, pesan: str) -> list[str]:
        if not isinstance(pesan, str):
            raise TypeError("pesan harus string")

        hasil: list[str] = []
        for obj in self._pengirim:
            if hasattr(obj, "kirim") and callable(getattr(obj, "kirim")):
                try:
                    out = obj.kirim(pesan)
                except TypeError:
                    continue
                hasil.append(str(out))
        return hasil


if __name__ == "__main__":
    notifier = Notifier()
    notifier.tambah_pengirim(EmailSender("service-email"))
    notifier.tambah_pengirim(SmsSender("service-sms"))
    notifier.tambah_pengirim(PushSender("service-push"))
    notifier.tambah_pengirim(BrokenSender())

    semua = notifier.kirim("Halo")
    for line in semua:
        print(line)