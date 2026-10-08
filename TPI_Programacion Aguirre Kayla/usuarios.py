import database


# ============================================================
# REGISTRAR USUARIO
# ============================================================

def registrar(nombre, usuario, password):

    if nombre == "" or usuario == "" or password == "":
        return False, "Todos los campos son obligatorios."

    if database.existe_usuario(usuario):
        return False, "El nombre de usuario ya existe."

    resultado = database.registrar_usuario(
        nombre,
        usuario,
        password
    )

    if resultado:
        return True, "Usuario registrado correctamente."

    return False, "No se pudo registrar el usuario."


# ============================================================
# INICIAR SESIÓN
# ============================================================

def iniciar_sesion(usuario, password):

    if usuario == "" or password == "":
        return None

    resultado = database.buscar_usuario(
        usuario,
        password
    )

    return resultado


# ============================================================
# COMPROBAR SI EXISTE USUARIO
# ============================================================

def usuario_existe(usuario):

    return database.existe_usuario(usuario)