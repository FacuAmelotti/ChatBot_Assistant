#pyinstaller --onefile --windowed
#pyinstaller --onefile --windowed --icon=icon.ico script.py
import tkinter as tk
import rivescript
from PIL import Image, ImageTk

color_fondo_usuario = 'gray10'
color_fondo_programa = 'gray15'

class ChatBot:
    def __init__(self):
        self.bot = rivescript.RiveScript()
        self.bot.load_file("config/respuestas.rive")
        self.bot.sort_replies()

    def reply(self, mensaje):
        return self.bot.reply("localuser", mensaje)

class InterfazGrafica:
    def __init__(self, master):
        self.master = master
        master.title("ChatBot - ByFacu")
        master.resizable(width=False, height=False)

        # Configurar widgets
        self.frame_mensajes = tk.Frame(self.master)
        self.frame_mensajes.pack(side=tk.TOP)

        self.scrollbar = tk.Scrollbar(self.frame_mensajes)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.consola = tk.Text(self.frame_mensajes, wrap=tk.WORD, yscrollcommand=self.scrollbar.set)
        self.consola.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.consola.configure(bg='gray15', fg='white')
        self.consola.config(state=tk.DISABLED)

        self.scrollbar.config(command=self.consola.yview)

        self.frame_entrada = tk.Frame(self.master)
        self.frame_entrada.pack(side=tk.BOTTOM)

        self.entrada = tk.Entry(self.frame_entrada, font=("Arial", 16))
        self.entrada.bind("<Return>", self.enviar_mensaje)
        self.entrada.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(5,5))
        self.entrada.configure(bg='gray25', fg='white')
        self.entrada.config(width=47, bg='gray10')
        self.entrada.focus_set()

        self.boton_resetear = tk.Button(self.frame_entrada, text="Clear", command=self.resetear_consola, bg='gray50', fg='white')
        self.boton_resetear.pack(side=tk.RIGHT, padx=(0,5))

        self.boton_enviar = tk.Button(self.frame_entrada, text="Enviar", command=self.enviar_mensaje, bg='gray50', fg='white')
        self.boton_enviar.pack(side=tk.RIGHT, padx=(0,5))

        self.imagen_usuario = ImageTk.PhotoImage(Image.open("imgs/imagen_usuario.png"))
        self.imagen_programa = ImageTk.PhotoImage(Image.open("imgs/imagen_programa.png"))
        self.imagen_reset = ImageTk.PhotoImage(Image.open("imgs/imagen_reset.png"))

        # Inicializar chatbot
        self.chatbot = ChatBot()

    def enviar_mensaje(self, event=None):
        mensaje = self.entrada.get()
        self.entrada.delete(0, tk.END)

        # Agregar mensaje de usuario en gris
        self.agregar_mensaje(mensaje, "gray", True)

        # Obtener respuesta del bot
        respuesta = self.chatbot.reply(mensaje)

        # Agregar respuesta en verde
        if not respuesta:
            self.agregar_mensaje("...", "green", False)
            with open('config/sinRespuestas.txt', 'a') as file:
                file.write(mensaje + "\n")
        else:
            self.agregar_mensaje(respuesta, "green", False)

    def agregar_mensaje(self, mensaje, color, es_usuario, es_reset=False):
        self.consola.config(state=tk.NORMAL)
        if color == 'gray':
            color_fondo = color_fondo_usuario
        else:
            color_fondo = color_fondo_programa

        self.consola.tag_config(color, foreground=color, background=color_fondo)
        imagen = self.imagen_usuario if es_usuario else (self.imagen_reset if es_reset else self.imagen_programa)
        self.consola.image_create(tk.END, image=imagen)
        self.consola.insert(tk.END, mensaje + "\n", color)
        self.consola.config(state=tk.DISABLED)
        self.consola.see(tk.END)

    def resetear_consola(self):
        self.consola.config(state=tk.NORMAL)
        self.consola.delete(1.0, tk.END)
        mensaje_reset = "Consola reseteada"
        self.agregar_mensaje(mensaje_reset, "deep sky blue", False, True)
        self.consola.config(state=tk.DISABLED)
                             
if __name__ == "__main__":
    root = tk.Tk()
    interfaz = InterfazGrafica(root)
    msg = " Bienvenido! \n * Soy un Bot y cumplo la tarea de Asistente virtual \n * Mi tarea es brindar informacion sobre mi creador: Facundo Ezequiel Amelotti \n >> Si quieres ver la Guia, tienes cualquier problema o alguna consulta, escribe 'help' \n >>> Escribeme algo en el recuadro inferior."
    interfaz.agregar_mensaje(msg, "green", "", es_reset=False)
    root.mainloop()