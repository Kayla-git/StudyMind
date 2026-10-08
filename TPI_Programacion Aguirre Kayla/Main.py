import tkinter as tk
from tkinter import messagebox

import usuarios
import materias


# ============================================================
# CONFIGURACIÓN
# ============================================================

NOMBRE_APP = "StudyMind"

ANCHO = 900
ALTO = 600


# ============================================================
# VENTANA PRINCIPAL
# ============================================================

class StudyMindApp:

    def __init__(self, root):

        self.root = root

        self.root.title(NOMBRE_APP)
        self.root.geometry(f"{ANCHO}x{ALTO}")
        self.root.resizable(False, False)

        # Usuario actualmente conectado
        self.usuario_actual = None

        # Mostrar pantalla inicial
        self.mostrar_bienvenida()


    # ========================================================
    # LIMPIAR PANTALLA
    # ========================================================

    def limpiar_pantalla(self):

        for widget in self.root.winfo_children():
            widget.destroy()


    # ========================================================
    # PANTALLA DE BIENVENIDA
    # ========================================================

    def mostrar_bienvenida(self):

        self.limpiar_pantalla()

        contenedor = tk.Frame(self.root)

        contenedor.pack(expand=True)

        titulo = tk.Label(
            contenedor,
            text="StudyMind",
            font=("Arial", 32, "bold")
        )

        titulo.pack(pady=20)

        subtitulo = tk.Label(
            contenedor,
            text="Tu espacio inteligente para aprender",
            font=("Arial", 15)
        )

        subtitulo.pack(pady=10)

        descripcion = tk.Label(
            contenedor,
            text=(
                "Organizá tus materias, realizá actividades\n"
                "y descubrí qué temas necesitás reforzar."
            ),
            font=("Arial", 12),
            justify="center"
        )

        descripcion.pack(pady=20)

        boton_ingresar = tk.Button(
            contenedor,
            text="Ingresar",
            width=20,
            height=2,
            command=self.mostrar_login
        )

        boton_ingresar.pack(pady=10)

        boton_registro = tk.Button(
            contenedor,
            text="Crear cuenta",
            width=20,
            height=2,
            command=self.mostrar_registro
        )

        boton_registro.pack(pady=10)


    # ========================================================
    # LOGIN
    # ========================================================

    def mostrar_login(self):

        self.limpiar_pantalla()

        titulo = tk.Label(
            self.root,
            text="Iniciar sesión",
            font=("Arial", 24, "bold")
        )

        titulo.pack(pady=40)

        formulario = tk.Frame(self.root)

        formulario.pack()

        tk.Label(
            formulario,
            text="Usuario:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        entrada_usuario = tk.Entry(
            formulario,
            width=30
        )

        entrada_usuario.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        tk.Label(
            formulario,
            text="Contraseña:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        entrada_password = tk.Entry(
            formulario,
            width=30,
            show="*"
        )

        entrada_password.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )


        # ----------------------------------------------------
        # INGRESAR
        # ----------------------------------------------------

        def ingresar():

            usuario = entrada_usuario.get().strip()
            password = entrada_password.get().strip()

            if usuario == "" or password == "":

                messagebox.showwarning(
                    "Datos incompletos",
                    "Completá usuario y contraseña."
                )

                return


            resultado = usuarios.iniciar_sesion(
                usuario,
                password
            )


            if resultado is None:

                messagebox.showerror(
                    "Error",
                    "Usuario o contraseña incorrectos."
                )

                return


            self.usuario_actual = resultado

            messagebox.showinfo(
                "Bienvenido",
                f"¡Hola, {resultado[1]}!"
            )

            self.mostrar_dashboard()


        boton = tk.Button(
            self.root,
            text="Ingresar",
            width=20,
            height=2,
            command=ingresar
        )

        boton.pack(pady=20)


        volver = tk.Button(
            self.root,
            text="Volver",
            command=self.mostrar_bienvenida
        )

        volver.pack()


    # ========================================================
    # REGISTRO
    # ========================================================

    def mostrar_registro(self):

        self.limpiar_pantalla()

        titulo = tk.Label(
            self.root,
            text="Crear cuenta",
            font=("Arial", 24, "bold")
        )

        titulo.pack(pady=30)

        formulario = tk.Frame(self.root)

        formulario.pack()


        # NOMBRE

        tk.Label(
            formulario,
            text="Nombre:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        entrada_nombre = tk.Entry(
            formulario,
            width=30
        )

        entrada_nombre.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )


        # USUARIO

        tk.Label(
            formulario,
            text="Usuario:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        entrada_usuario = tk.Entry(
            formulario,
            width=30
        )

        entrada_usuario.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )


        # CONTRASEÑA

        tk.Label(
            formulario,
            text="Contraseña:"
        ).grid(
            row=2,
            column=0,
            padx=10,
            pady=10
        )

        entrada_password = tk.Entry(
            formulario,
            width=30,
            show="*"
        )

        entrada_password.grid(
            row=2,
            column=1,
            padx=10,
            pady=10
        )


        # ----------------------------------------------------
        # REGISTRAR
        # ----------------------------------------------------

        def registrar():

            nombre = entrada_nombre.get().strip()
            usuario = entrada_usuario.get().strip()
            password = entrada_password.get().strip()


            if (
                nombre == ""
                or usuario == ""
                or password == ""
            ):

                messagebox.showwarning(
                    "Datos incompletos",
                    "Completá todos los campos."
                )

                return


            resultado, mensaje = usuarios.registrar(
                nombre,
                usuario,
                password
            )


            if resultado:

                messagebox.showinfo(
                    "Registro exitoso",
                    mensaje
                )

                self.mostrar_login()

            else:

                messagebox.showerror(
                    "No se pudo registrar",
                    mensaje
                )


        boton_registrar = tk.Button(
            self.root,
            text="Registrarse",
            width=20,
            height=2,
            command=registrar
        )

        boton_registrar.pack(pady=20)


        volver = tk.Button(
            self.root,
            text="Volver",
            command=self.mostrar_bienvenida
        )

        volver.pack()


    # ========================================================
    # DASHBOARD
    # ========================================================

    def mostrar_dashboard(self):

        self.limpiar_pantalla()


        # ENCABEZADO

        encabezado = tk.Frame(self.root)

        encabezado.pack(
            fill="x",
            padx=30,
            pady=20
        )


        titulo = tk.Label(
            encabezado,
            text="StudyMind",
            font=("Arial", 24, "bold")
        )

        titulo.pack(side="left")


        nombre_usuario = self.usuario_actual[1]


        usuario = tk.Label(
            encabezado,
            text=f"Usuario: {nombre_usuario}",
            font=("Arial", 11)
        )

        usuario.pack(side="right")


        # BIENVENIDA

        bienvenida = tk.Label(
            self.root,
            text=f"¡Hola, {nombre_usuario}! 👋",
            font=("Arial", 20, "bold")
        )

        bienvenida.pack(pady=20)


        descripcion = tk.Label(
            self.root,
            text="¿Qué querés hacer hoy?",
            font=("Arial", 13)
        )

        descripcion.pack(pady=5)


        # MENÚ

        menu = tk.Frame(self.root)

        menu.pack(pady=30)


        # MATERIAS

        boton_materias = tk.Button(
            menu,
            text="📚 Mis materias",
            width=25,
            height=3,
            command=self.mostrar_materias
        )

        boton_materias.grid(
            row=0,
            column=0,
            padx=15,
            pady=15
        )


        # ACTIVIDADES

        boton_actividades = tk.Button(
            menu,
            text="📝 Actividades",
            width=25,
            height=3,
            command=self.mostrar_actividades
        )

        boton_actividades.grid(
            row=0,
            column=1,
            padx=15,
            pady=15
        )


        # PROGRESO

        boton_progreso = tk.Button(
            menu,
            text="📊 Mi progreso",
            width=25,
            height=3,
            command=self.mostrar_progreso
        )

        boton_progreso.grid(
            row=1,
            column=0,
            padx=15,
            pady=15
        )


        # RECOMENDACIONES

        boton_recomendaciones = tk.Button(
            menu,
            text="🧠 Recomendaciones",
            width=25,
            height=3,
            command=self.mostrar_recomendaciones
        )

        boton_recomendaciones.grid(
            row=1,
            column=1,
            padx=15,
            pady=15
        )


        # CERRAR SESIÓN

        cerrar = tk.Button(
            self.root,
            text="Cerrar sesión",
            command=self.cerrar_sesion
        )

        cerrar.pack(pady=20)


    # ========================================================
    # MATERIAS
    # ========================================================

    def mostrar_materias(self):

        self.limpiar_pantalla()


        titulo = tk.Label(
            self.root,
            text="Mis materias",
            font=("Arial", 24, "bold")
        )

        titulo.pack(pady=30)


        # ----------------------------------------------------
        # FORMULARIO
        # ----------------------------------------------------

        formulario = tk.Frame(self.root)

        formulario.pack(pady=10)


        tk.Label(
            formulario,
            text="Nueva materia:"
        ).grid(
            row=0,
            column=0,
            padx=10
        )


        entrada_materia = tk.Entry(
            formulario,
            width=30
        )

        entrada_materia.grid(
            row=0,
            column=1,
            padx=10
        )


        # ----------------------------------------------------
        # AGREGAR
        # ----------------------------------------------------

        def agregar():

            nombre = entrada_materia.get().strip()


            if nombre == "":

                messagebox.showwarning(
                    "Campo vacío",
                    "Escribí el nombre de la materia."
                )

                return


            resultado = materias.agregar(nombre)


            if resultado:

                messagebox.showinfo(
                    "Materia agregada",
                    "La materia se agregó correctamente."
                )

                self.mostrar_materias()

            else:

                messagebox.showwarning(
                    "Error",
                    "No se pudo agregar la materia."
                )


        boton_agregar = tk.Button(
            formulario,
            text="➕ Agregar materia",
            command=agregar
        )

        boton_agregar.grid(
            row=0,
            column=2,
            padx=10
        )


        # ----------------------------------------------------
        # LISTA
        # ----------------------------------------------------

        tk.Label(
            self.root,
            text="Materias disponibles:",
            font=("Arial", 14, "bold")
        ).pack(pady=20)


        lista_materias = materias.obtener_todas()


        if len(lista_materias) == 0:

            tk.Label(
                self.root,
                text="Todavía no hay materias cargadas."
            ).pack(pady=10)


        else:

            for materia in lista_materias:

                tk.Label(
                    self.root,
                    text="📚 " + materia[1],
                    font=("Arial", 12)
                ).pack(pady=3)


        # ----------------------------------------------------
        # VOLVER
        # ----------------------------------------------------

        tk.Button(
            self.root,
            text="Volver",
            command=self.mostrar_dashboard
        ).pack(pady=25)


    # ========================================================
    # ACTIVIDADES
    # ========================================================

    def mostrar_actividades(self):

        self.limpiar_pantalla()


        tk.Label(
            self.root,
            text="Actividades",
            font=("Arial", 24, "bold")
        ).pack(pady=40)


        tk.Label(
            self.root,
            text=(
                "Acá aparecerán las actividades disponibles\n"
                "según las materias del estudiante."
            ),
            font=("Arial", 12),
            justify="center"
        ).pack(pady=20)


        tk.Button(
            self.root,
            text="Comenzar actividad",
            width=25,
            height=2
        ).pack(pady=20)


        tk.Button(
            self.root,
            text="Volver",
            command=self.mostrar_dashboard
        ).pack(pady=20)


    # ========================================================
    # PROGRESO
    # ========================================================

    def mostrar_progreso(self):

        self.limpiar_pantalla()


        tk.Label(
            self.root,
            text="Mi progreso",
            font=("Arial", 24, "bold")
        ).pack(pady=40)


        tk.Label(
            self.root,
            text="Progreso general",
            font=("Arial", 14, "bold")
        ).pack(pady=10)


        tk.Label(
            self.root,
            text="Actividades realizadas: 0"
        ).pack(pady=5)


        tk.Label(
            self.root,
            text="Respuestas correctas: 0"
        ).pack(pady=5)


        tk.Label(
            self.root,
            text="Rendimiento: 0%"
        ).pack(pady=5)


        tk.Button(
            self.root,
            text="Volver",
            command=self.mostrar_dashboard
        ).pack(pady=30)


    # ========================================================
    # RECOMENDACIONES
    # ========================================================

    def mostrar_recomendaciones(self):

        self.limpiar_pantalla()


        tk.Label(
            self.root,
            text="Recomendaciones",
            font=("Arial", 24, "bold")
        ).pack(pady=40)


        tk.Label(
            self.root,
            text=(
                "StudyMind analizará tu rendimiento para\n"
                "recomendarte qué temas deberías reforzar."
            ),
            font=("Arial", 12),
            justify="center"
        ).pack(pady=20)


        tk.Label(
            self.root,
            text="💡 Todavía no hay suficientes datos.",
            font=("Arial", 13)
        ).pack(pady=20)


        tk.Button(
            self.root,
            text="Volver",
            command=self.mostrar_dashboard
        ).pack(pady=30)


    # ========================================================
    # CERRAR SESIÓN
    # ========================================================

    def cerrar_sesion(self):

        respuesta = messagebox.askyesno(
            "Cerrar sesión",
            "¿Seguro que querés cerrar sesión?"
        )


        if respuesta:

            self.usuario_actual = None

            self.mostrar_bienvenida()


# ============================================================
# EJECUCIÓN DEL PROGRAMA
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = StudyMindApp(root)

    root.mainloop()
