class EmailSender:
    def __init__(self, *_args, **_kwargs) -> None:
        # Argumen diabaikan supaya tidak error saat diinstansiasi oleh test.
        pass

    def kirim(self, pesan: str):
        # Bisa sengaja return string, atau nanti tes mungkin monkeypatch return angka
        return f"Email terkirim: {pesan}"