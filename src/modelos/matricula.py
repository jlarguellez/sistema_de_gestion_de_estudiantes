"""Modelo Matricula: relaciona un estudiante con un curso y guarda su nota."""

from datetime import date

NOTA_MINIMA = 0.0
NOTA_MAXIMA = 5.0


class Matricula:
    def __init__(self, estudiante, curso):
        self.estudiante = estudiante
        self.curso = curso
        self.fecha = date.today()
        self.nota = None

    def asignar_nota(self, valor):
        """Registra la nota validando que esté entre 0.0 y 5.0."""
        if not NOTA_MINIMA <= valor <= NOTA_MAXIMA:
            raise ValueError(
                f"La nota debe estar entre {NOTA_MINIMA} y {NOTA_MAXIMA}"
            )
        self.nota = valor

    def __str__(self):
        nota = self.nota if self.nota is not None else "sin nota"
        return f"{self.estudiante} | {self.curso} | {nota}"
