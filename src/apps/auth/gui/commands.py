from tkinter import messagebox

from ttkbootstrap import Entry, Toplevel, Window

from apps.main.gui.windows import create_main_window


def login(root: Window, window: Toplevel, email_entry: Entry, password_entry: Entry) -> None:
    email = email_entry.get()
    password = password_entry.get()

    if not email or not password:
        messagebox.showerror('Ошибка', 'Заполните все поля!')
        return

    window.destroy()
    create_main_window(root, email)
