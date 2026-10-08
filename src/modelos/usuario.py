"""Modelo Usuario: cuenta de acceso al Sistema de Gestión de Estudiantes (SGE)."""

import hashlib
import hmac
import os

ROLES_VALIDOS = ("administrador", "docente", "estudiante")
ITERACIONES = 100_000


def _cifrar(contrasena, sal):
    """Devuelve el hash PBKDF2 de la contraseña usando la sal dada."""
    return hashlib.pbkdf2_hmac(
        "sha256", contrasena.encode("utf-8"), sal, ITERACIONES
    )


class Usuario:
    def __init__(self, nombre_usuario, contrasena, rol):
        if rol not in ROLES_VALIDOS:
            raise ValueError(f"Rol inválido. Opciones: {', '.join(ROLES_VALIDOS)}")
        if not nombre_usuario:
            raise ValueError("El nombre de usuario es obligatorio")
        if len(contrasena) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres")
        self.nombre_usuario = nombre_usuario
        self.rol = rol
        self._sal = os.urandom(16)
        self._contrasena_hash = _cifrar(contrasena, self._sal)
        self.sesion_activa = False

    def verificar_contrasena(self, contrasena):
        """Compara la contraseña ingresada con el hash guardado."""
        hash_ingresado = _cifrar(contrasena, self._sal)
        return hmac.compare_digest(hash_ingresado, self._contrasena_hash)

    def iniciar_sesion(self, contrasena):
        """Inicia sesión si la contraseña es correcta. Devuelve True o False."""
        self.sesion_activa = self.verificar_contrasena(contrasena)
        return self.sesion_activa

    def cerrar_sesion(self):
        self.sesion_activa = False

    def tiene_rol(self, rol):
        return self.rol == rol

    def __str__(self):
        return f"{self.nombre_usuario} ({self.rol})"
