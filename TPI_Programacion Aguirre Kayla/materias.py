import database

# ============================================================
# AGREGAR MATERIA
# ============================================================

def agregar(nombre):

    if nombre == "":
        return False

    database.agregar_materia(nombre)

    return True


# ============================================================
# OBTENER MATERIAS
# ============================================================

def obtener_todas():

    return database.obtener_materias()


# ============================================================
# BUSCAR MATERIA
# ============================================================

def buscar_por_id(materia_id):
    materias = database.obtener_materias()

    for materia in materias:

        if materia[0] == materia_id:
            return materia

    return None
