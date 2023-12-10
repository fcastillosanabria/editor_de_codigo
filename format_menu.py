from tkinter import *
from tkinter import ttk
from tkinter.font import Font

current_font_size = 16  # Tamaño de fuente inicial

def change_font(text_widget):
    font = fontchooser.askfont()
    if font:
        text_widget.tag_configure("custom", font=font)
        text_widget.configure(font=font)

def change_text_color(text_widget):
    color = colorchooser.askcolor()[1]
    if color:
        text_widget.tag_add("color", text_widget.index(SEL_FIRST), text_widget.index(SEL_LAST))
        text_widget.tag_config("color", foreground=color)

def toggle_dark_mode(text_widget, dark_mode_var):
    if dark_mode_var.get():
        text_widget.configure(bg="black", fg="white")
        text_widget.tk_setPalette(background="black", foreground="white")
        text_widget.vbar.configure(bg="white")  # Configurar el fondo de la barra de desplazamiento vertical
    else:
        text_widget.configure(bg="white", fg="black")
        text_widget.tk_setPalette(background="white", foreground="black")
        text_widget.vbar.configure(bg="gray")  # Restaurar el color de fondo de la barra de desplazamiento vertical

# def toggle_dark_mode(text_widget, dark_mode_var):
#     if dark_mode_var.get():
#         text_widget.configure(bg="black", fg="white")
#         text_widget.tk_setPalette(background="black", foreground="white")
#         text_widget.vbar.configure(troughcolor="gray", bordercolor="black")
#     else:
#         text_widget.configure(bg="white", fg="black")
#         text_widget.tk_setPalette(background="white", foreground="black")
#         text_widget.vbar.configure(troughcolor="gray", bordercolor="white")


def change_font_size(text_widget, size_delta):
    global current_font_size
    new_size = current_font_size + size_delta
    if new_size > 0:
        current_font_size = new_size
        current_font = text_widget.tag_cget("custom", "font")
        font_family = Font(font=current_font).actual()['family']
        new_font = Font(family=font_family, size=current_font_size)
        text_widget.configure(font=new_font)

def main(root, text_widget, menubar):
    format_menu = Menu(menubar, tearoff=0)  # tearoff=0 evita que se pueda despegar el menú
    menubar.add_cascade(label="Formato", menu=format_menu)

    format_menu.add_command(label="Cambiar Fuente", command=lambda: change_font(text_widget))
    format_menu.add_command(label="Cambiar Color de Texto", command=lambda: change_text_color(text_widget))
    format_menu.add_separator()

    # Variable de control para el Modo Oscuro
    dark_mode_var = BooleanVar()
    format_menu.add_checkbutton(label="Modo Oscuro", variable=dark_mode_var, command=lambda: toggle_dark_mode(text_widget, dark_mode_var))

    format_menu.add_separator()

    # Crear un menú desplegable persistente para cambiar el tamaño de la fuente
    font_size_menu = Menu(format_menu, tearoff=0)  # tearoff=0 evita que se pueda despegar el menú
    format_menu.add_cascade(label="Cambiar Tamaño", menu=font_size_menu)

    # Opciones para cambiar el tamaño de la fuente
    font_size_menu.add_command(label="16 px", command=lambda: set_font_size(16))
    font_size_menu.add_command(label="20 px", command=lambda: set_font_size(20))
    font_size_menu.add_command(label="24 px", command=lambda: set_font_size(24))
    font_size_menu.add_command(label="28 px", command=lambda: set_font_size(28))
    font_size_menu.add_command(label="32 px", command=lambda: set_font_size(32))
    font_size_menu.add_command(label="36 px", command=lambda: set_font_size(36))
    font_size_menu.add_command(label="40 px", command=lambda: set_font_size(40))
    font_size_menu.add_command(label="44 px", command=lambda: set_font_size(44))
    font_size_menu.add_command(label="48 px", command=lambda: set_font_size(48))
    font_size_menu.add_command(label="52 px", command=lambda: set_font_size(52))
    font_size_menu.add_command(label="Aumentar Tamaño", command=lambda: change_font_size(text_widget, 4))
    font_size_menu.add_command(label="Disminuir Tamaño", command=lambda: change_font_size(text_widget, -4))

    # Función para cambiar el tamaño de la fuente
    def set_font_size(size):
        global current_font_size
        current_font_size = size
        current_font = text_widget.tag_cget("custom", "font")
        font_family = Font(font=current_font).actual()['family']
        new_font = Font(family=font_family, size=current_font_size)
        text_widget.configure(font=new_font)

    root.config(menu=menubar)