import sqlite3


# ============================================================
# CONFIGURACIÓN
# ============================================================

NOMBRE_BD = "studymind.db"


# ============================================================
# CONEXIÓN
# ============================================================

def conectar():

    conexion = sqlite3.connect(NOMBRE_BD)

    return conexion


# ============================================================
# CREAR TABLAS
# ============================================================

def crear_tablas():

    conexion = conectar()
    cursor = conexion.cursor()

    # TABLA USUARIOS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            usuario TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)

    # TABLA MATERIAS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS materias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
    """)

    # TABLA ACTIVIDADES
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS actividades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            materia_id INTEGER NOT NULL,
            titulo TEXT NOT NULL,
            descripcion TEXT,
            FOREIGN KEY (materia_id) REFERENCES materias(id)
        )
    """)

    # TABLA RESULTADOS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resultados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            actividad_id INTEGER NOT NULL,
            respuestas_correctas INTEGER NOT NULL,
            total_preguntas INTEGER NOT NULL,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
            FOREIGN KEY (actividad_id) REFERENCES actividades(id)
        )
    """)

    conexion.commit()
    conexion.close()


# ============================================================
# REGISTRAR USUARIO
# ============================================================

def registrar_usuario(nombre, usuario, password):

    conexion = conectar()
    cursor = conexion.cursor()

    try:

        cursor.execute("""
            INSERT INTO usuarios (nombre, usuario, password)
            VALUES (?, ?, ?)
        """, (nombre, usuario, password))

        conexion.commit()

        return True

    except sqlite3.IntegrityError:

        return False

    finally:

        conexion.close()


# ============================================================
# BUSCAR USUARIO
# ============================================================

def buscar_usuario(usuario, password):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, nombre, usuario
        FROM usuarios
        WHERE usuario = ? AND password = ?
    """, (usuario, password))

    resultado = cursor.fetchone()

    conexion.close()

    return resultado


# ============================================================
# COMPROBAR SI EXISTE USUARIO
# ============================================================

def existe_usuario(usuario):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id
        FROM usuarios
        WHERE usuario = ?
    """, (usuario,))

    resultado = cursor.fetchone()

    conexion.close()

    return resultado is not None


# ============================================================
# AGREGAR MATERIA
# ============================================================

def agregar_materia(nombre):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO materias (nombre)
        VALUES (?)
    """, (nombre,))

    conexion.commit()
    conexion.close()


# ============================================================
# OBTENER MATERIAS
# ============================================================

def obtener_materias():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, nombre
        FROM materias
        ORDER BY nombre
    """)

    materias = cursor.fetchall()

    conexion.close()

    return materias


# ============================================================
# AGREGAR ACTIVIDAD
# ============================================================

def agregar_actividad(materia_id, titulo, descripcion):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO actividades (
            materia_id,
            titulo,
            descripcion
        )
        VALUES (?, ?, ?)
    """, (materia_id, titulo, descripcion))

    conexion.commit()
    conexion.close()


# ============================================================
# OBTENER ACTIVIDADES
# ============================================================

def obtener_actividades(materia_id):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, titulo, descripcion
        FROM actividades
        WHERE materia_id = ?
    """, (materia_id,))

    actividades = cursor.fetchall()

    conexion.close()

    return actividades


# ============================================================
# GUARDAR RESULTADO
# ============================================================

def guardar_resultado(
    usuario_id,
    actividad_id,
    respuestas_correctas,
    total_preguntas
):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO resultados (
            usuario_id,
            actividad_id,
            respuestas_correctas,
            total_preguntas
        )
        VALUES (?, ?, ?, ?)
    """, (
        usuario_id,
        actividad_id,
        respuestas_correctas,
        total_preguntas
    ))

    conexion.commit()
    conexion.close()


# ============================================================
# OBTENER RESULTADOS
# ============================================================

def obtener_resultados(usuario_id):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            id,
            actividad_id,
            respuestas_correctas,
            total_preguntas
        FROM resultados
        WHERE usuario_id = ?
    """, (usuario_id,))

    resultados = cursor.fetchall()

    conexion.close()

    return resultados


# ============================================================
# INICIALIZAR BASE DE DATOS
# ============================================================

crear_tablas()