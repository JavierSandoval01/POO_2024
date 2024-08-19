# trabajadores/login.py
import hashlib
from conexionBD import *

@staticmethod
def login_admin(usuario, contrasena):
    try:
        contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
        cursor.execute(
        "select * from administrador where usuario=%s and password=%s",
        (usuario,contrasena)
        )
        usuario=cursor.fetchone()
        if usuario:
            return usuario
        else:
            return None
    except:
        return None

@staticmethod
def login_mesero(usuario, contrasena):
    try:
        contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
        cursor.execute(
        "select * from mesero where usuario=%s and password=%s",
        (usuario,contrasena)
        )
        usuario=cursor.fetchone()
        if usuario:
            return usuario
        else:
            return None
    except:
        return None