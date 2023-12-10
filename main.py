from tkinter import *
from tkinter.font import Font  # Importa la clase Font desde tkinter.font
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
import file_menu
import edit_menu
import format_menu
import help_menu

root = Tk()

root.title("Text Editor-Untiltled")
root.geometry("300x250+300+300")
root.minsize(width=400, height=400)

# Configurar la fuente inicial
default_font = Font(family="Courier New", size=16)

# Crear el widget de texto y configurar la fuente inicial
text = ScrolledText(root, state='normal', height=400, width=400, wrap='word', pady=2, padx=3, undo=True, font=default_font)
text.pack(fill=Y, expand=1)
text.focus_set()

# Configurar el tag 'custom' inicialmente con la misma fuente
text.tag_configure("custom", font=default_font)

menubar = Menu(root)

file_menu.main(root, text, menubar)
edit_menu.main(root, text, menubar)
format_menu.main(root, text, menubar)
help_menu.main(root, text, menubar)
root.mainloop()