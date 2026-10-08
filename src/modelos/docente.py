"""Modelo Docente del Sistema de Gestión de Estudiantes (SGE)."""


class Docente:
    def __init__(self, documento, nombres, apellidos, correo=None):
        if not documento:
            raise ValueError("El documento es obligatorio")
        self.documento = documento
        self.nombres = nombres
        self.apellidos = apellidos
        self.correo = correo
        self.cursos = []

    @property
    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"

    def agregar_curso(self, curso):
        """Registra un curso dictado por el docente (sin duplicados)."""
        if curso not in self.cursos:
            self.cursos.append(curso)

    def registrar_nota(self, matricula, valor):
        """Registra la nota de una matrícula, solo si el curso es del docente."""
        if matricula.curso not in self.cursos:
            raise PermissionError("El docente no dicta este curso")
        matricula.asignar_nota(valor)

    def __str__(self):
        return f"{self.documento} - {self.nombre_completo}"
