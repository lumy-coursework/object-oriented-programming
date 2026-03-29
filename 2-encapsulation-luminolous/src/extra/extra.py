from math import ceil
from typing import Dict, List


class ChatPromptManager:
    DEFAULT_SYSTEM = "You are a helpful AI assistant."
    def __init__(self, model_name: str = "gpt-4o-mini", 
                 temperature: float = 1.0, max_tokens: int = 1024, 
                 system_prompt: str = DEFAULT_SYSTEM,) -> None:

        self._model_name: str = str(model_name).strip() or "gpt-4o-mini"
        self._temperature: float = 1.0
        self._max_tokens: int = 1024
        self._system_prompt: str = ""
        self._messages: List[Dict[str, str]] = []

        self.temperature = temperature
        self.max_tokens = max_tokens
        self.system_prompt = system_prompt

    @property
    def model_name(self) -> str:
        return self._model_name

    @model_name.setter
    def model_name(self, value: str) -> None:
        self._model_name = str(value).strip() or "gpt-4o-mini"

    @property
    def temperature(self) -> float:
        return self._temperature

    @temperature.setter
    def temperature(self, value: float) -> None:
        try:
            v = float(value)
        except (TypeError, ValueError):
            v = 1.0
        self._temperature = max(0.0, min(2.0, v))

    @property
    def max_tokens(self) -> int:
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, value: int) -> None:
        try:
            v = int(value)
        except (TypeError, ValueError):
            v = 1024
        self._max_tokens = max(1, v)

    @property
    def system_prompt(self) -> str:
        return self._system_prompt

    @system_prompt.setter
    def system_prompt(self, value: str) -> None:
        text = ("" if value is None else str(value)).strip()
        self._system_prompt = text or self.DEFAULT_SYSTEM

    @property
    def messages(self) -> List[Dict[str, str]]:
        return [dict(m) for m in self._messages]

    @staticmethod
    def _normalize_text(text: str) -> str:
        return ("" if text is None else str(text)).strip()

    def add_user(self, text: str) -> None:
        text = self._normalize_text(text)
        if not text:
            return
        self._messages.append({"role": "user", "content": text})

    def add_assistant(self, text: str) -> None:
        text = self._normalize_text(text)
        if not text:
            return
        self._messages.append({"role": "assistant", "content": text})

    def clear(self) -> None:
        self._messages.clear()

    @staticmethod
    def _estimate_tokens_for_text(text: str) -> int:
        words = [w for w in ChatPromptManager._normalize_text(text).split() if w]
        return int(ceil(len(words) * 1.3)) or (1 if text else 0)

    def _messages_token_overhead(self) -> int:
        return 8 + 4 * len(self._messages)

    def estimate_total_tokens(self) -> int:
        total = self._messages_token_overhead()
        total += self._estimate_tokens_for_text(self.system_prompt)
        for m in self._messages:
            total += self._estimate_tokens_for_text(m["content"])
        return total

    def remaining_tokens(self) -> int:
        return max(0, self.max_tokens - self.estimate_total_tokens())

    def _build_messages_with_system(self) -> List[Dict[str, str]]:
        return [{"role": "system", "content": self.system_prompt}, *self.messages]

    def build_payload(self, trim_to_fit: bool = True) -> Dict:
        msgs = self._build_messages_with_system()

        if trim_to_fit:
            def count_msgs_tokens(seq: List[Dict[str, str]]) -> int:
                total = 0
                total += 4 * len(seq)
                for m in seq:
                    total += self._estimate_tokens_for_text(m["content"])
                return total

            while count_msgs_tokens(msgs) > self.max_tokens and len(msgs) > 1:
                msgs.pop(1)

        payload = {
            "model": self.model_name,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "messages": msgs,
        }
        return payload

if __name__ == "__main__":
    print("ChatPromptManager")
    mgr = ChatPromptManager(max_tokens=1000, system_prompt="You are a domain expert in AI.")
    mgr.add_user("Ringkas apa itu LLM dalam 2 kalimat.")
    mgr.add_assistant("LLM adalah model pembelajaran mesin besar yang dilatih pada "
                      "jumlah data teks masif untuk memprediksi token berikutnya.")
    mgr.add_user("Sebutkan 3 contoh use-case singkat.")
    mgr.add_assistant("1) Asisten penulisan, 2) tanya-jawab, 3) ekstraksi informasi.")
    mgr.add_user("Jabarkan tiap poin jadi satu kalimat.")

    print("Objek:", mgr)
    print("Estimasi token:", mgr.estimate_total_tokens())
    print("Sisa token:", mgr.remaining_tokens())

    payload = mgr.build_payload(trim_to_fit=True)
    print("\nPayload:")
    import json as _json
    print(_json.dumps(payload, indent=2, ensure_ascii=False))

    print("\nTotal pesan yang dikirim:", len(payload["messages"]))