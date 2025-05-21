from functools import partial

import ttkbootstrap as ttk
from ttkbootstrap import Window

from apps.auth.gui.commands import login


def create_login_window(root: Window) -> None:
    login_window = ttk.Toplevel(root)
    login_window.title('Авторизация')
    login_window.geometry('400x300')
    login_window.resizable(False, False)

    outer_frame = ttk.Frame(login_window)
    outer_frame.grid(row=0, column=0, sticky='nsew')
    login_window.grid_rowconfigure(0, weight=1)
    login_window.grid_columnconfigure(0, weight=1)

    frame = ttk.Frame(outer_frame, padding=20)
    frame.grid(row=0, column=0, sticky='n')
    outer_frame.grid_rowconfigure(0, weight=1)
    outer_frame.grid_columnconfigure(0, weight=1)

    style = ttk.Style()
    style.configure('TLabel', font=('Arial', 12), padding=5, foreground='#e0e0e0')
    style.configure('TButton', font=('Arial', 11), padding=8)
    style.configure('Title.TLabel', font=('Arial', 16, 'bold'), padding=10, foreground='#ffffff')

    title_label = ttk.Label(frame, text='Вход в MailSender', style='Title.TLabel')
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    email_label = ttk.Label(frame, text='Email:')
    email_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
    email_entry = ttk.Entry(frame, width=30, style='primary.TEntry')
    email_entry.grid(row=1, column=1, padx=10, pady=5)

    password_label = ttk.Label(frame, text='Пароль:')
    password_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
    password_entry = ttk.Entry(frame, width=30, show='*', style='primary.TEntry')
    password_entry.grid(row=2, column=1, padx=10, pady=5)

    login_button = ttk.Button(
        frame,
        text='Войти',
        style='primary.Outline.TButton',
        command=partial(login, root, login_window, email_entry, password_entry),
    )
    login_button.grid(row=3, column=0, columnspan=2, pady=20)
