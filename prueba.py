from modelos.estudiante import Estudiante
from modelos.docente import Docente
from modelos.curso import Curso
from modelos.matricula import Matricula

est = Estudiante("100", "Ana", "Pérez", "ana@correo.com")
doc = Docente("200", "Luis", "Gómez")
curso = Curso("SW101", "Entornos de desarrollo", 3)
curso.asignar_docente(doc)

mat = Matricula(est, curso)
est.agregar_matricula(mat)
doc.registrar_nota(mat, 4.5)
print(est, "| promedio:", est.obtener_promedio())