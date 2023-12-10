from tkinter import *
from tkinter.messagebox import showinfo

def show_about_dialog():
    showinfo("Acerca de", "Editor de Texto\nVersión 1.0\nDesarrollado por Tu Nombre")

def main(root, text_widget, menubar):
    help_menu = Menu(menubar)
    menubar.add_cascade(label="Help", menu=help_menu)

    help_menu.add_command(label="About", command=show_about_dialog)

    root.config(menu=menubar)
