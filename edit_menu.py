from tkinter import *

def cut_text(text_widget):
    text_widget.event_generate("<<Cut>>")

def copy_text(text_widget):
    text_widget.event_generate("<<Copy>>")

def paste_text(text_widget):
    text_widget.event_generate("<<Paste>>")

def undo(text_widget):
    text_widget.event_generate("<<Undo>>")

def redo(text_widget):
    text_widget.event_generate("<<Redo>>")

def main(root, text_widget, menubar):
    edit_menu = Menu(menubar)
    menubar.add_cascade(label="Editar", menu=edit_menu)

    edit_menu.add_command(label="Cortar", command=lambda: cut_text(text_widget))
    edit_menu.add_command(label="Copiar", command=lambda: copy_text(text_widget))
    edit_menu.add_command(label="Pegar", command=lambda: paste_text(text_widget))
    edit_menu.add_separator()
    edit_menu.add_command(label="Deshacer", command=lambda: undo(text_widget))
    edit_menu.add_command(label="Rehacer", command=lambda: redo(text_widget))

    root.config(menu=menubar)
