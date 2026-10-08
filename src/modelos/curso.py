"""Modelo Curso del Sistema de Gestión de Estudiantes (SGE)."""


class Curso:
    def __init__(self, codigo, nombre, creditos):
        if not codigo:
            raise ValueError("El código del curso es obligatorio")
        if creditos <= 0:
            raise ValueError("Los créditos deben ser mayores que cero")
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.activo = True
        self.docente = None

    def asignar_docente(self, docente):
        """Asigna el docente que dicta el curso."""
        self.docente = docente
        docente.agregar_curso(self)

    def desactivar(self):
        self.activo = False

    def activar(self):
        self.activo = True

    def __str__(self):
        return f"{self.codigo} - {self.nombre} ({self.creditos} créditos)"
