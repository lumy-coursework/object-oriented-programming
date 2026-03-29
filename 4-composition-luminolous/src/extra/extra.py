"""
Student
- Kegunaan: merepresentasikan mahasiswa.
- Atribut: _name: str, _student_id: str (trim spasi).
- Properti: name, student_id (getter & setter).
- Metode: label() → "{student_id} - {name}".

GradePolicy
- Kegunaan: menyimpan bobot komponen penilaian dan menghitung skor akhir.
- Atribut: _weights: dict[str, float] dengan syarat:
    - Semua nilai bobot ≥ 0 dan jumlah bobot = 1.0 (±1e-6).
    - Nama komponen di-trim; kunci harus unik.
- Properti: weights (getter & setter), components (getter).
- Metode:
    - compute(scores: dict[str, float]) -> float → jumlah weight * score (score diambil 0 bila tidak ada).
    - missing_components(scores) -> list[str] → komponen yang belum ada nilainya.

Enrollment (komposisi Student + GradePolicy)
- Kegunaan: menyimpan nilai per komponen untuk seorang mahasiswa sesuai kebijakan bobot, lalu menghitung nilai akhir.
- Atribut: _student: Student, _policy: GradePolicy, _scores: dict[str, float].
- Properti: student (getter & setter, validasi tipe), policy (getter & setter, validasi tipe).
- Metode:
    - set_score(component: str, value: float) -> None
      Validasi: komponen harus ada di policy; skor dibatasi ke rentang 0–100.
    - get_score(component: str) -> float | None
    - final_score() -> float → memakai GradePolicy.compute.
    - report() -> str → ringkasan nilai, bobot, komponen yang belum terisi.
- Aturan khusus:
    - Menolak komponen yang tidak terdefinisi di GradePolicy (raise ValueError).
    - Menolak tipe objek yang salah untuk student / policy (raise TypeError).
"""

from __future__ import annotations
from typing import Dict, List

class Student:
    """
    Representasi mahasiswa.
    - name: nama mahasiswa (string, di-trim)
    - student_id: NIM/ID (string, di-trim)
    """

    def __init__(self, name: str, student_id: str) -> None:
        self.name = name
        self.student_id = student_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = (value or "").strip()

    @property
    def student_id(self) -> str:
        return self._student_id

    @student_id.setter
    def student_id(self, value: str) -> None:
        self._student_id = (value or "").strip()

    def label(self) -> str:
        return f"{self._student_id} - {self._name}"

    def __repr__(self) -> str:
        return f"Student(name={self._name!r}, student_id={self._student_id!r})"


class GradePolicy:
    """
    Kebijakan bobot penilaian.
    - weights: dict nama_komponen -> bobot (float)
      * bobot >= 0
      * jumlah bobot = 1.0 (toleransi 1e-6)
      * nama komponen di-trim dan unik
    """

    def __init__(self, weights: Dict[str, float]) -> None:
        self.weights = weights

    @property
    def weights(self) -> Dict[str, float]:
        return self._weights

    @weights.setter
    def weights(self, value: Dict[str, float]) -> None:
        if not isinstance(value, dict):
            raise TypeError("weights harus dict[str, float].")

        cleaned: Dict[str, float] = {}
        for k, v in value.items():
            key = (k or "").strip()
            if key == "":
                raise ValueError("Nama komponen tidak boleh kosong.")
            if key in cleaned:
                raise ValueError(f"Duplikasi komponen: {key!r}.")
            try:
                w = float(v)
            except Exception as e:
                raise TypeError(f"Bobot untuk {key!r} harus float.") from e
            if w < 0:
                raise ValueError(f"Bobot {key!r} harus >= 0.")
            cleaned[key] = w

        total = sum(cleaned.values())
        if abs(total - 1.0) > 1e-6:
            raise ValueError(f"Jumlah bobot harus 1.0, saat ini {total:.6f}.")

        self._weights = cleaned

    @property
    def components(self) -> List[str]:
        return list(self._weights.keys())

    def compute(self, scores: Dict[str, float]) -> float:
        """
        Hitung nilai akhir: sum(w_i * score_i).
        Komponen yang tidak ada pada scores dianggap 0.
        """
        total = 0.0
        for comp, w in self._weights.items():
            s = float(scores.get(comp, 0.0))
            total += w * s
        return total

    def missing_components(self, scores: Dict[str, float]) -> List[str]:
        return [c for c in self._weights if c not in scores]


class Enrollment:
    """
    Komposisi:
    - student: Student
    - policy: GradePolicy
    - scores: dict komponen -> skor (0..100)
    """

    def __init__(self, student: Student, policy: GradePolicy) -> None:
        self.student = student
        self.policy = policy
        self._scores: Dict[str, float] = {}

    @property
    def student(self) -> Student:
        return self._student

    @student.setter
    def student(self, value: Student) -> None:
        if not isinstance(value, Student):
            raise TypeError("student harus bertipe Student.")
        self._student = value

    @property
    def policy(self) -> GradePolicy:
        return self._policy

    @policy.setter
    def policy(self, value: GradePolicy) -> None:
        if not isinstance(value, GradePolicy):
            raise TypeError("policy harus bertipe GradePolicy.")
        self._policy = value

    def set_score(self, component: str, value: float) -> None:
        """
        Set skor untuk sebuah komponen.
        - Komponen harus terdaftar di policy.
        - Skor dibatasi ke [0, 100].
        """
        comp = (component or "").strip()
        if comp not in self._policy.components:
            raise ValueError(
                f"Komponen {comp!r} tidak ada pada GradePolicy. "
                f"Tersedia: {', '.join(self._policy.components)}"
            )
        try:
            val = float(value)
        except Exception as e:
            raise TypeError("value harus numerik.") from e

        if val < 0:
            val = 0.0
        elif val > 100:
            val = 100.0

        self._scores[comp] = val

    def get_score(self, component: str) -> float | None:
        comp = (component or "").strip()
        return self._scores.get(comp)

    def final_score(self) -> float:
        return self._policy.compute(self._scores)

    def report(self) -> str:
        """
        Laporan nilai per komponen + bobot + nilai akhir.
        Menunjukkan penggunaan kembali:
          - Student.label()
          - GradePolicy.compute() & missing_components()
        """
        lines: List[str] = []
        lines.append(f"Student: {self._student.label()}")
        lines.append("Komponen:")
        for comp in self._policy.components:
            w = self._policy.weights[comp]
            s = self._scores.get(comp, None)
            s_txt = f"{s:.1f}/100" if s is not None else "(belum diisi)"
            lines.append(f"  - {comp}: {s_txt} (bobot {w:.2f})")

        miss = self._policy.missing_components(self._scores)
        if miss:
            lines.append(f"Belum diisi: {', '.join(miss)}")

        lines.append(f"Nilai akhir: {self.final_score():.2f}")
        return "\n".join(lines)

    def __repr__(self) -> str:
        return f"Enrollment(student={self._student!r}, policy={self._policy!r}, scores={self._scores!r})"


if __name__ == "__main__":
    mhs = Student("  Siti Nurhaliza  ", "  5025211234 ")

    policy = GradePolicy({
        "Tugas": 0.30,
        "UTS":   0.30,
        "UAS":   0.40,
    })

    enr = Enrollment(mhs, policy)

    enr.set_score("Tugas", 88.4)
    enr.set_score("UTS", 76.2)
    enr.set_score("UAS", 91.0)

    print(enr.report())