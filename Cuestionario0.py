import tkinter as tk
from tkinter import ttk, messagebox
import platform

# -------------------- CONFIGURACIÓN --------------------
INTENTOS_MAX = 3
intentos_actuales = 0
mejor_puntaje = 0
mejor_detalle = []

# -------------------- PREGUNTAS --------------------
PREGUNTAS = [
    {
        "texto": "¿Cuál era una debilidad criptográfica fundamental de la máquina Enigma causada por su reflector (Umkehrwalze)?",
        "opciones": [
            "El reflector podía ser removido fácilmente",
            "Una letra nunca podía ser cifrada como ella misma",
            "Solo funcionaba con el alfabeto alemán",
            "El reflector se movía durante el cifrado"
        ],
        "respuesta": "Una letra nunca podía ser cifrada como ella misma",
        "explicacion": "El reflector emparejaba contactos eléctricos, lo que impedía que una letra se cifrara como sí misma — una debilidad crucial explotada por los Aliados."
    },
    {
        "texto": "¿Cuántos rotores podían seleccionarse en la Enigma M4 de la Kriegsmarine y cuántos se insertaban a la vez?",
        "opciones": [
            "5 rotores disponibles, 3 insertados",
            "8 rotores disponibles, 3 insertados",
            "8 rotores disponibles, 4 insertados",
            "10 rotores disponibles, 4 insertados"
        ],
        "respuesta": "8 rotores disponibles, 4 insertados",
        "explicacion": "La Enigma M4 tenía 8 rotores disponibles, de los cuales 4 se utilizaban simultáneamente para cifrar mensajes navales."
    },
    {
        "texto": "¿Qué es la 'anomalía del doble paso' (double-stepping anomaly) en la máquina Enigma?",
        "opciones": [
            "Los rotores podían girar en ambas direcciones",
            "El rotor del medio avanzaba dos veces en pulsaciones sucesivas bajo ciertas condiciones",
            "Cada rotor avanzaba dos posiciones por cada tecla presionada",
            "El plugboard duplicaba las conexiones eléctricas"
        ],
        "respuesta": "El rotor del medio avanzaba dos veces en pulsaciones sucesivas bajo ciertas condiciones",
        "explicacion": "La anomalía ocurría cuando el rotor central estaba en una posición de muesca que causaba dos movimientos consecutivos, reduciendo el ciclo del cifrado."
    },
    {
        "texto": "¿Cuántos cables de conexión (plugs) se emitían típicamente con cada máquina Enigma para usar en el Steckerbrett (plugboard)?",
        "opciones": ["6 cables", "8 cables", "10 cables", "13 cables"],
        "respuesta": "10 cables",
        "explicacion": "Las Enigma militares contaban con 10 cables, permitiendo 10 pares de letras intercambiadas antes y después del paso por los rotores."
    },
    {
        "texto": "¿Qué máquina diseñó Alan Turing en Bletchley Park para acelerar el proceso de descifrado de los ajustes de Enigma?",
        "opciones": ["La máquina Colossus", "La máquina ACE", "La Bombe", "La máquina Universal"],
        "respuesta": "La Bombe",
        "explicacion": "Alan Turing diseñó la 'Bombe', una máquina electromecánica que ayudó a descifrar los códigos alemanes de Enigma."
    },
    {
        "texto": "¿En qué año publicó Alan Turing su paper 'On Computable Numbers, with an Application to the Entscheidungsproblem'?",
        "opciones": ["1933", "1936", "1940", "1950"],
        "respuesta": "1936",
        "explicacion": "Turing publicó este trabajo en 1936, sentando las bases de la teoría de la computación con su modelo de máquina abstracta."
    },
    {
        "texto": "¿Cuáles son los componentes principales de una máquina de Turing según su definición formal?",
        "opciones": [
            "Una CPU, RAM y disco duro",
            "Una cinta infinita, un cabezal de lectura/escritura y un conjunto de estados finitos",
            "Un teclado, pantalla y procesador",
            "Rotores, reflector y plugboard"
        ],
        "respuesta": "Una cinta infinita, un cabezal de lectura/escritura y un conjunto de estados finitos",
        "explicacion": "El modelo formal de Turing consta de una cinta infinita, un cabezal lector/escritor y un conjunto finito de estados."
    },
    {
        "texto": "¿Qué es el 'problema de la parada' (halting problem) que Turing demostró?",
        "opciones": [
            "El problema de parar una máquina Enigma",
            "La imposibilidad de crear un algoritmo general que determine si cualquier programa terminará o se ejecutará indefinidamente",
            "Un error en el diseño de las máquinas de Turing",
            "El problema de detener computadoras físicas"
        ],
        "respuesta": "La imposibilidad de crear un algoritmo general que determine si cualquier programa terminará o se ejecutará indefinidamente",
        "explicacion": "Turing probó que no existe un algoritmo universal capaz de determinar si un programa terminará o no su ejecución."
    },
    {
        "texto": "¿Qué propone la tesis de Church-Turing?",
        "opciones": [
            "Que las computadoras nunca podrán pensar",
            "Que cualquier función calculable por un método efectivo puede ser calculada por una máquina de Turing",
            "Que las máquinas de Turing son más rápidas que las computadoras modernas",
            "Que solo existen funciones computables"
        ],
        "respuesta": "Que cualquier función calculable por un método efectivo puede ser calculada por una máquina de Turing",
        "explicacion": "La tesis de Church-Turing afirma que toda función calculable efectivamente puede ser representada por una máquina de Turing."
    },
    {
        "texto": "¿Qué publicó Alan Turing en 1950 que introdujo lo que ahora se conoce como el 'Test de Turing'?",
        "opciones": [
            "On Computable Numbers",
            "Computing Machinery and Intelligence",
            "The Chemical Basis of Morphogenesis",
            "A Note on the Entscheidungsproblem"
        ],
        "respuesta": "Computing Machinery and Intelligence",
        "explicacion": "En 1950, Turing presentó 'Computing Machinery and Intelligence', donde propuso su famoso 'Juego de la Imitación'."
    }
]

# -------------------- INTERFAZ --------------------
def crear_root():
    root = tk.Tk()
    root.title("Cuestionario — Enigma y Máquina de Turing")
    root.geometry("980x740")
    root.configure(bg="#11111b")
    root.resizable(False, False)
    return root


def crear_titulo(root):
    tk.Label(
        root,
        text="🧠 Cuestionario — Enigma y Máquina de Turing",
        font=("Georgia", 22, "bold"),
        bg="#11111b",
        fg="#F5F5F7"
    ).pack(pady=10)


def crear_scroll_area(root):
    cont = tk.Frame(root, bg="#11111b")
    cont.pack(fill="both", expand=True, padx=15, pady=10)
    canvas = tk.Canvas(cont, bg="#11111b", highlightthickness=0)
    frame = tk.Frame(canvas, bg="#11111b")
    canvas.create_window((0, 0), window=frame, anchor="nw")

    def scroll(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    root.bind_all("<MouseWheel>", scroll)
    frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.pack(fill="both", expand=True)
    return frame


def mostrar_preguntas(frame):
    respuestas = []
    for i, p in enumerate(PREGUNTAS):
        marco = tk.LabelFrame(
            frame,
            text=f"Pregunta {i + 1}",
            bg="#1B1B2F",
            fg="#EAEAEA",
            font=("Helvetica", 11, "bold"),
            padx=10,
            pady=10
        )
        marco.pack(fill="x", pady=10)

        tk.Label(
            marco,
            text=p["texto"],
            wraplength=850,
            justify="left",
            bg="#1B1B2F",
            fg="#F0F0F0",
            font=("Arial", 11, "bold")
        ).pack(anchor="w", pady=5)

        var = tk.StringVar(value="")  # Ninguna seleccionada
        respuestas.append(var)

        for opcion in p["opciones"]:
            tk.Radiobutton(
                marco,
                text=opcion,
                variable=var,
                value=opcion,
                bg="#1B1B2F",
                fg="#DADADA",
                selectcolor="#2E2E42",
                activebackground="#2E2E42",
                anchor="w",
                padx=20,
                font=("Arial", 10)
            ).pack(fill="x", pady=2)
    return respuestas


# -------------------- FUNCIONALIDAD --------------------
def evaluar(root, respuestas):
    global intentos_actuales, mejor_puntaje, mejor_detalle

    # Validar que todas las preguntas tengan respuesta
    for i, var in enumerate(respuestas):
        if not var.get():
            messagebox.showwarning(
                "Falta responder",
                f"⚠️ Debes responder todas las preguntas antes de continuar.\n\nFalta la pregunta {i + 1}."
            )
            return

    puntaje = 0
    detalle = []

    for i, p in enumerate(PREGUNTAS):
        seleccion = respuestas[i].get()
        correcta = p["respuesta"]
        acierto = (seleccion == correcta)
        if acierto:
            puntaje += 1
        detalle.append({
            "numero": i + 1,
            "texto": p["texto"],
            "usuario": seleccion,
            "correcta": correcta,
            "explicacion": p["explicacion"],
            "acierto": acierto
        })

    if puntaje > mejor_puntaje:
        mejor_puntaje = puntaje
        mejor_detalle = detalle

    intentos_actuales += 1

    if puntaje == len(PREGUNTAS):
        messagebox.showinfo("¡Perfecto!", "🎉 ¡Todas las respuestas son correctas!\nMostrando resultados...")
        mostrar_resultados(root, puntaje, detalle)
        reiniciar_intentos()
        return

    if intentos_actuales < INTENTOS_MAX:
        messagebox.showinfo(
            "Intento registrado",
            f"Has completado el intento {intentos_actuales}/{INTENTOS_MAX}.\n"
            "Puedes intentar nuevamente para mejorar tu puntaje."
        )
        for var in respuestas:
            var.set("")
    else:
        mostrar_resultados(root, mejor_puntaje, mejor_detalle)
        reiniciar_intentos()


def reiniciar_intentos():
    global intentos_actuales, mejor_puntaje, mejor_detalle
    intentos_actuales = 0
    mejor_puntaje = 0
    mejor_detalle = []


def mostrar_resultados(root, puntaje, detalle):
    ventana = tk.Toplevel(root)
    ventana.title("Resultados y Retroalimentación")
    ventana.geometry("940x700")
    ventana.configure(bg="#0F1126")

    # Título principal
    tk.Label(
        ventana,
        text="📋 Retroalimentación — Enigma y Máquina de Turing",
        font=("Georgia", 20, "bold"),
        bg="#0F1126",
        fg="#F7F7FB"
    ).pack(pady=10)

    tk.Label(
        ventana,
        text=f"Puntaje final: {puntaje}/{len(PREGUNTAS)}",
        font=("Arial", 13, "bold"),
        bg="#0F1126",
        fg="#C0C8FF"
    ).pack(pady=5)

    frame_box = tk.Frame(ventana, bg="#0F1126")
    frame_box.pack(fill="both", expand=True, padx=15, pady=10)

    texto = tk.Text(
        frame_box,
        wrap="word",
        bg="#181A35",
        fg="#EAEAFF",
        font=("Consolas", 11),
        padx=15,
        pady=10
    )
    texto.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(frame_box, command=texto.yview)
    scrollbar.pack(side="right", fill="y")
    texto.configure(yscrollcommand=scrollbar.set)

    # Escribir resultados
    for item in detalle:
        resultado = "✅ Correcta" if item["acierto"] else "❌ Incorrecta"
        texto.insert("end", f"\n𝗣𝗿𝗲𝗴𝘂𝗻𝘁𝗮 {item['numero']}:\n", "titulo")
        texto.insert("end", f"  {item['texto']}\n\n", "normal")
        texto.insert("end", f"  ➤ Tu respuesta: {item['usuario']}\n", "respuesta")
        texto.insert("end", f"  ✔ Respuesta correcta: {item['correcta']}\n", "correcta")
        texto.insert("end", f"  {resultado}\n", "resultado")
        texto.insert("end", "\n  🧠 Explicación:\n", "subtitulo")
        texto.insert("end", f"     {item['explicacion']}\n", "explicacion")
        texto.insert("end", "\n" + "-" * 90 + "\n", "separador")

    texto.tag_configure("titulo", font=("Arial", 11, "bold"))
    texto.tag_configure("subtitulo", font=("Arial", 10, "bold italic"))
    texto.tag_configure("explicacion", lmargin1=25, lmargin2=25, spacing3=8)
    texto.config(state="disabled")

    tk.Button(
        ventana,
        text="Cerrar",
        command=ventana.destroy,
        bg="#6C63FF",
        fg="white",
        font=("Arial", 12, "bold"),
        relief="flat",
        padx=15,
        pady=5
    ).pack(pady=10)


# -------------------- MAIN --------------------
def main():
    root = crear_root()
    crear_titulo(root)
    area = crear_scroll_area(root)
    respuestas = mostrar_preguntas(area)

    tk.Button(
        root,
        text="Enviar respuestas",
        command=lambda: evaluar(root, respuestas),
        bg="#6C63FF",
        fg="white",
        font=("Arial", 13, "bold"),
        relief="flat",
        padx=20,
        pady=8
    ).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
