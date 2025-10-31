import tkinter as tk
from tkinter import ttk, messagebox

# -------------------- CONFIGURACIÓN --------------------
INTENTOS_MAX = 3
intentos_actuales = 0
mejor_puntaje = 0
mejor_detalle = []

# -------------------- PREGUNTAS --------------------
PREGUNTAS = [
    {
        "texto": "¿Cuál era una debilidad criptográfica fundamental de la máquina Enigma causada por su reflector (Umkehrwalze)?    ",
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
        "texto": "¿Cuántos rotores podían seleccionarse en la Enigma M4 de la Kriegsmarine y cuántos se insertaban a la vez?               ",
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
        "texto": "¿Qué es la 'anomalía del doble paso' (double-stepping anomaly) en la máquina Enigma?                                               ",
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
        "texto": "¿Cuántos cables de conexión (plugs) se emitían típicamente con cada máquina Enigma para usar en el Steckerbrett (plugboard)?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ",
        "opciones": ["6 cables", "8 cables", "10 cables", "13 cables                                                                                                                                                                            "],
        "respuesta": "10 cables",
        "explicacion": "Las Enigma militares contaban con 10 cables, permitiendo 10 pares de letras intercambiadas antes y después del paso por los rotores."
    },
    {
        "texto": "¿Qué máquina diseñó Alan Turing en Bletchley Park para acelerar el proceso de descifrado de los ajustes de Enigma?   ",
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
        "texto": "¿Cuáles son los componentes principales de una máquina de Turing según su definición formal?                                    ",
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
        "texto": "¿Qué propone la tesis de Church-Turing?                                                                                                                                                                                                                                                                                                                                                                                         ",
        "opciones": [
            "Que las computadoras nunca podrán pensar",
            "Que cualquier función calculable por un método efectivo puede ser calculada por una máquina de Turing                               ",
            "Que las máquinas de Turing son más rápidas que las computadoras modernas",
            "Que solo existen funciones computables"
        ],
        "respuesta": "Que cualquier función calculable por un método efectivo puede ser calculada por una máquina de Turing",
        "explicacion": "La tesis de Church-Turing afirma que toda función calculable efectivamente puede ser representada por una máquina de Turing."
    },
    {
        "texto": "¿Qué publicó Alan Turing en 1950 que introdujo lo que ahora se conoce como el 'Test de Turing'?                                ",
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
    root.geometry("950x740")
    root.configure(bg="#000000")
    root.resizable(False, False)
    return root


def crear_titulo(root):
    frame_titulo = tk.Frame(root, bg="#000000")
    frame_titulo.pack(pady=20)
    
    tk.Label(
        frame_titulo,
        text="🧠 Cuestionario — Enigma y Máquina de Turing",
        font=("Segoe UI", 22, "bold"),
        bg="#000000",
        fg="#FFFFFF"
    ).pack()


def crear_scroll_area(root):
    # Estilo de scrollbar oscuro
    style = ttk.Style()
    style.theme_use("clam")  # necesario para poder editar colores
    style.configure(
    "Vertical.TScrollbar",
    gripcount=0,
    background="#2E2E2E",     # color del "track" (zona deslizable)
    darkcolor="#1F1F1F",      # bordes más oscuros
    lightcolor="#3A3A3A",     # bordes claros
    troughcolor="#0F0F0F",    # fondo de la pista
    bordercolor="#1F1F1F",
    arrowcolor="#B0B0B0"      # color de las flechas
)
    # Frame contenedor principal
    cont = tk.Frame(root, bg="#000000")
    cont.pack(fill="both", expand=True, padx=20, pady=(0, 15))
    
    # Canvas y scrollbar
    canvas = tk.Canvas(cont, bg="#000000", highlightthickness=0)
    scrollbar = ttk.Scrollbar(cont, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#000000")
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Empaquetar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Scroll con rueda del mouse
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    canvas.bind_all("<MouseWheel>", _on_mousewheel)
    
    return scrollable_frame


def crear_pregunta_card(parent, numero, pregunta_data, var):
    """Crea una tarjeta de pregunta con bordes redondeados y altura uniforme"""
    # Canvas contenedor
    canvas = tk.Canvas(parent, bg="#000000", highlightthickness=0)
    canvas.pack(fill="x", pady=10, padx=10, expand=True)

    # Frame principal
    card = tk.Frame(canvas, bg="#1C1C1C", relief="flat", bd=0)
    card_window = canvas.create_window((10, 10), window=card, anchor="nw")

    # Header con número
    header_frame = tk.Frame(card, bg="#1C1C1C")
    header_frame.pack(fill="x", padx=25, pady=(20, 10))

    badge_canvas = tk.Canvas(header_frame, bg="#1C1C1C", highlightthickness=0, width=40, height=30)
    badge_canvas.pack(side="left")
    badge_canvas.create_oval(2, 2, 38, 28, fill="#7C3AED", outline="")
    badge_canvas.create_text(20, 15, text=f"{numero}", font=("Segoe UI", 10, "bold"), fill="#FFFFFF")

    # Texto de la pregunta
    tk.Label(
        card,
        text=pregunta_data["texto"],
        wraplength=850,
        justify="left",
        bg="#1C1C1C",
        fg="#FFFFFF",
        font=("Segoe UI", 11),
        anchor="w"
    ).pack(anchor="w", padx=25, pady=(0, 15))

    # Opciones
    opciones_frame = tk.Frame(card, bg="#1C1C1C")
    opciones_frame.pack(fill="x", padx=25, pady=(0, 20))

    for opcion in pregunta_data["opciones"]:
        rb = tk.Radiobutton(
            opciones_frame,
            text=opcion,
            variable=var,
            value=opcion,
            bg="#1C1C1C",
            fg="#FFFFFF",
            selectcolor="#2A2A2A",
            activebackground="#1C1C1C",
            activeforeground="#FFFFFF",
            font=("Segoe UI", 10),
            anchor="w",
            padx=10,
            pady=8,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            cursor="hand2"
        )
        rb.pack(fill="x", pady=2)

        def on_enter(e, widget=rb): widget.config(fg="#FFFFFF")
        def on_leave(e, widget=rb): widget.config(fg="#FFFFFF")
        rb.bind("<Enter>", on_enter)
        rb.bind("<Leave>", on_leave)

    # Dibujo del borde redondeado
    def actualizar_borde(altura_fija=None):
        canvas.delete("borde")
        w = card.winfo_reqwidth() + 20
        h = altura_fija if altura_fija else card.winfo_reqheight() + 20
        r = 15
        canvas.create_arc(0, 0, 2*r, 2*r, start=90, extent=90, fill="#1C1C1C", outline="", tags="borde")
        canvas.create_arc(w-2*r, 0, w, 2*r, start=0, extent=90, fill="#1C1C1C", outline="", tags="borde")
        canvas.create_arc(0, h-2*r, 2*r, h, start=180, extent=90, fill="#1C1C1C", outline="", tags="borde")
        canvas.create_arc(w-2*r, h-2*r, w, h, start=270, extent=90, fill="#1C1C1C", outline="", tags="borde")
        canvas.create_rectangle(r, 0, w-r, h, fill="#1C1C1C", outline="", tags="borde")
        canvas.create_rectangle(0, r, w, h-r, fill="#1C1C1C", outline="", tags="borde")
        canvas.configure(width=w, height=h)
        canvas.tag_lower("borde")

    card.actualizar_borde = actualizar_borde  # guardar método para igualar después
    card.bind("<Configure>", lambda e: actualizar_borde())
    return card, canvas


def mostrar_preguntas(frame):
    """Crea todas las preguntas y ajusta alturas uniformes"""
    respuestas = []
    tarjetas = []  # almacenar referencias a las tarjetas

    for i, pregunta in enumerate(PREGUNTAS):
        var = tk.StringVar(value="_none_")  # valor imposible, indica “no seleccionado”

        respuestas.append(var)
        card, canvas = crear_pregunta_card(frame, i + 1, pregunta, var)
        tarjetas.append((card, canvas))

    # Calcular la altura máxima de todas las tarjetas
    frame.update_idletasks()
    max_altura = max(card.winfo_reqheight() + 20 for card, _ in tarjetas)

    # Ajustar todas las tarjetas a esa altura
    for card, canvas in tarjetas:
        card.actualizar_borde(altura_fija=max_altura)

    return respuestas


# -------------------- FUNCIONALIDAD --------------------
def evaluar(root, respuestas):
    global intentos_actuales, mejor_puntaje, mejor_detalle

    # Verificar que todas las preguntas estén respondidas
    for i, var in enumerate(respuestas):
        if not var.get():
            messagebox.showwarning(
                "Falta responder",
                f"⚠ Debes responder todas las preguntas antes de continuar.\n\nFalta la pregunta {i + 1}."
            )
            return

    # Calcular puntaje
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

    # Actualizar mejor puntaje
    if puntaje > mejor_puntaje:
        mejor_puntaje = puntaje
        mejor_detalle = detalle

    intentos_actuales += 1

    # Verificar si es perfecto
    if puntaje == len(PREGUNTAS):
        messagebox.showinfo("¡Perfecto!", "🎉 ¡Todas las respuestas son correctas!\nMostrando resultados...")
        mostrar_resultados(root, puntaje, detalle)
        reiniciar_intentos()
        return

    # Verificar intentos restantes
    if intentos_actuales < INTENTOS_MAX:
        messagebox.showinfo(
            "Intento registrado",
            f"Has completado el intento {intentos_actuales}/{INTENTOS_MAX}.\n"
            "Puedes intentar nuevamente para mejorar tu puntaje."
        )
        # Limpiar respuestas
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
    ventana.configure(bg="#000000")

    # Título
    tk.Label(
        ventana,
        text="📋 Retroalimentación",
        font=("Segoe UI", 22, "bold"),
        bg="#000000",
        fg="#FFFFFF"
    ).pack(pady=20)

    # Puntaje destacado con bordes redondeados
    puntaje_canvas = tk.Canvas(ventana, bg="#000000", highlightthickness=0, height=60)
    puntaje_canvas.pack(pady=(0, 15))
    
    # Dibujar rectángulo redondeado para el puntaje
    def draw_rounded_rect(canvas, x1, y1, x2, y2, r, **kwargs):
        points = [x1+r, y1,
                  x2-r, y1,
                  x2, y1,
                  x2, y1+r,
                  x2, y2-r,
                  x2, y2,
                  x2-r, y2,
                  x1+r, y2,
                  x1, y2,
                  x1, y2-r,
                  x1, y1+r,
                  x1, y1]
        return canvas.create_polygon(points, **kwargs, smooth=True)
    
    draw_rounded_rect(puntaje_canvas, 10, 10, 250, 50, 15, fill="#1C1C1C", outline="")
    puntaje_canvas.create_text(130, 30, 
                               text=f"Puntaje final: {puntaje}/{len(PREGUNTAS)}", 
                               font=("Segoe UI", 14, "bold"), 
                               fill="#7C3AED")

    # Frame con scroll para detalles
    frame_box = tk.Frame(ventana, bg="#000000")
    frame_box.pack(fill="both", expand=True, padx=20, pady=(0, 15))

    texto = tk.Text(
        frame_box,
        wrap="word",
        bg="#1C1C1C",
        fg="#FFFFFF",
        font=("Segoe UI", 10),
        padx=20,
        pady=15,
        relief="flat",
        borderwidth=0,
        highlightthickness=0
    )
    texto.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(frame_box, command=texto.yview)
    scrollbar.pack(side="right", fill="y")
    texto.configure(yscrollcommand=scrollbar.set)

    # Configurar tags para formato
    texto.tag_config("titulo", font=("Segoe UI", 12, "bold"), foreground="#FFFFFF", spacing3=5)
    texto.tag_config("normal", font=("Segoe UI", 10), foreground="#B0B0B0", spacing3=10)
    texto.tag_config("respuesta", font=("Segoe UI", 10), foreground="#909090")
    texto.tag_config("correcta", font=("Segoe UI", 10, "bold"), foreground="#7C3AED")
    texto.tag_config("resultado_ok", font=("Segoe UI", 10, "bold"), foreground="#10B981")
    texto.tag_config("resultado_error", font=("Segoe UI", 10, "bold"), foreground="#EF4444")
    texto.tag_config("subtitulo", font=("Segoe UI", 10, "bold"), foreground="#60A5FA")
    texto.tag_config("explicacion", font=("Segoe UI", 10), foreground="#B0B0B0", spacing3=15)

    # Insertar resultados
    for item in detalle:
        resultado_tag = "resultado_ok" if item["acierto"] else "resultado_error"
        resultado_texto = "✅ Correcta" if item["acierto"] else "❌ Incorrecta"
        
        texto.insert("end", f"Pregunta {item['numero']}\n", "titulo")
        texto.insert("end", f"{item['texto']}\n\n", "normal")
        texto.insert("end", f"Tu respuesta: {item['usuario']}\n", "respuesta")
        texto.insert("end", f"Respuesta correcta: {item['correcta']}\n", "correcta")
        texto.insert("end", f"{resultado_texto}\n\n", resultado_tag)
        texto.insert("end", "💡 Explicación\n", "subtitulo")
        texto.insert("end", f"{item['explicacion']}\n\n", "explicacion")
        texto.insert("end", "─" * 90 + "\n\n", "normal")

    texto.config(state="disabled")

    # Botón cerrar con bordes redondeados
    boton_frame = tk.Frame(ventana, bg="#000000")
    boton_frame.pack(pady=15)
    
    boton_canvas = tk.Canvas(boton_frame, bg="#000000", highlightthickness=0, width=120, height=45)
    boton_canvas.pack()
    
    def crear_boton_redondeado(canvas, estado="normal"):
        canvas.delete("all")
        color = "#6D28D9" if estado == "hover" else "#7C3AED"
        draw_rounded_rect(canvas, 0, 0, 120, 45, 10, fill=color, outline="")
        canvas.create_text(60, 22, text="Cerrar", font=("Segoe UI", 12, "bold"), fill="#FFFFFF")
    
    crear_boton_redondeado(boton_canvas)
    
    def on_enter(e):
        crear_boton_redondeado(boton_canvas, "hover")
    
    def on_leave(e):
        crear_boton_redondeado(boton_canvas)
    
    def on_click(e):
        ventana.destroy()
    
    boton_canvas.bind("<Enter>", on_enter)
    boton_canvas.bind("<Leave>", on_leave)
    boton_canvas.bind("<Button-1>", on_click)
    boton_canvas.configure(cursor="hand2")


# -------------------- MAIN --------------------
def main():
    root = crear_root()
    crear_titulo(root)
    area = crear_scroll_area(root)
    respuestas = mostrar_preguntas(area)

    # Botón enviar con bordes redondeados y efecto hover
    boton_frame = tk.Frame(root, bg="#000000")
    boton_frame.pack(pady=15)
    
    boton_canvas = tk.Canvas(boton_frame, bg="#000000", highlightthickness=0, width=200, height=50)
    boton_canvas.pack()
    
    def crear_boton_redondeado(canvas, estado="normal"):
        canvas.delete("all")
        color = "#6D28D9" if estado == "hover" else "#7C3AED"
        # Crear rectángulo redondeado
        r = 12
        w, h = 200, 50
        canvas.create_arc(0, 0, 2*r, 2*r, start=90, extent=90, fill=color, outline="")
        canvas.create_arc(w-2*r, 0, w, 2*r, start=0, extent=90, fill=color, outline="")
        canvas.create_arc(0, h-2*r, 2*r, h, start=180, extent=90, fill=color, outline="")
        canvas.create_arc(w-2*r, h-2*r, w, h, start=270, extent=90, fill=color, outline="")
        canvas.create_rectangle(r, 0, w-r, h, fill=color, outline="")
        canvas.create_rectangle(0, r, w, h-r, fill=color, outline="")
        canvas.create_text(100, 25, text="Enviar respuestas", font=("Segoe UI", 13, "bold"), fill="#FFFFFF")
    
    crear_boton_redondeado(boton_canvas)
    
    def on_enter(e):
        crear_boton_redondeado(boton_canvas, "hover")
    
    def on_leave(e):
        crear_boton_redondeado(boton_canvas)
    
    def on_click(e):
        evaluar(root, respuestas)
    
    boton_canvas.bind("<Enter>", on_enter)
    boton_canvas.bind("<Leave>", on_leave)
    boton_canvas.bind("<Button-1>", on_click)
    boton_canvas.configure(cursor="hand2")

    root.mainloop()


if __name__ == "__main__":
    main()