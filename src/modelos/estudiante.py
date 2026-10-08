"""Modelo Estudiante del Sistema de Gestión de Estudiantes (SGE)."""


class Estudiante:
    def __init__(self, documento, nombres, apellidos, correo):
        if not documento:
            raise ValueError("El documento es obligatorio")
        self.documento = documento
        self.nombres = nombres
        self.apellidos = apellidos
        self.correo = correo
        self.matriculas = []

    @property
    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"

    def agregar_matricula(self, matricula):
        """Asocia una matrícula al estudiante evitando duplicados por curso."""
        for m in self.matriculas:
            if m.curso == matricula.curso:
                raise ValueError("El estudiante ya está matriculado en este curso")
        self.matriculas.append(matricula)

    def obtener_promedio(self):
        """Promedio de las notas registradas (0.0 si no hay ninguna)."""
        notas = [m.nota for m in self.matriculas if m.nota is not None]
        return sum(notas) / len(notas) if notas else 0.0

    def __str__(self):
        return f"{self.documento} - {self.nombre_completo}"
