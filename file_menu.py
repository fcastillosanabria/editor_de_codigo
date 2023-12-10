from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(text_widget):
    file_path = askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_widget.delete(1.0, END)
            text_widget.insert(END, file.read())

def save_file(text_widget):
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_widget.get(1.0, END))

def exit_app(root):
    root.quit()

def main(root, text_widget, menubar):
    file_menu = Menu(menubar)
    menubar.add_cascade(label="Archivo", menu=file_menu)

    file_menu.add_command(label="Abrir", command=lambda: open_file(text_widget))
    file_menu.add_command(label="Guardar", command=lambda: save_file(text_widget))
    file_menu.add_separator()
    file_menu.add_command(label="Salir", command=lambda: exit_app(root))

    root.config(menu=menubar)
