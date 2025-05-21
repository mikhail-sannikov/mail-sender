import tkinter as tk
from functools import partial

import ttkbootstrap as ttk
from ttkbootstrap import Window

from apps.main.gui import commands


def create_main_window(root: Window, sender_email: str) -> None:
    root.deiconify()
    root.title('Отправка письма')
    root.geometry('700x400')
    root.resizable(False, False)

    # Контейнер для центрирования
    outer_frame = ttk.Frame(root)
    outer_frame.grid(row=0, column=0, sticky='nsew')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Внутренний фрейм
    frame = ttk.Frame(outer_frame, padding=20)
    frame.grid(row=0, column=0, sticky='n')
    outer_frame.grid_rowconfigure(0, weight=1)
    outer_frame.grid_columnconfigure(0, weight=1)

    style = ttk.Style()
    style.configure('TLabel', font=('Arial', 12), padding=5, foreground='#e0e0e0')
    style.configure('TButton', font=('Arial', 11), padding=8)
    style.configure('Title.TLabel', font=('Arial', 16, 'bold'), padding=10, foreground='#ffffff')
    style.configure('secondary.TLabel', foreground='#b0b0b0')

    title_label = ttk.Label(frame, text='Рассылка почты', style='Title.TLabel')
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    emails_file_path = tk.StringVar(value='Файл с почтами не выбран')
    html_file_path = tk.StringVar(value='HTML файл не выбран')

    emails_label = ttk.Label(frame, text='Файл с почтами (Excel):')
    emails_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')

    emails_file_button = ttk.Button(
        frame,
        text='Выбрать файл с почтами',
        style='primary.TButton',
        command=partial(commands.choose_emails_file, emails_file_path),
    )
    emails_file_button.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

    emails_file_status = ttk.Label(frame, textvariable=emails_file_path, style='secondary.TLabel', wraplength=400)
    emails_file_status.grid(row=2, column=0, columnspan=2, padx=10, pady=(0, 10), sticky='w')

    html_label = ttk.Label(frame, text='HTML файл письма:')
    html_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')

    html_file_button = ttk.Button(
        frame,
        text='Выбрать HTML файл',
        style='primary.TButton',
        command=partial(commands.choose_html_file, html_file_path),
    )
    html_file_button.grid(row=3, column=1, padx=10, pady=5, sticky='ew')

    html_file_status = ttk.Label(frame, textvariable=html_file_path, style='secondary.TLabel', wraplength=400)
    html_file_status.grid(row=4, column=0, columnspan=2, padx=10, pady=(0, 20), sticky='w')

    send_button = ttk.Button(
        frame,
        text='Отправить письма',
        style='primary.Outline.TButton',
        command=partial(commands.send, emails_file_path, html_file_path, sender_email),
    )
    send_button.grid(row=5, column=0, columnspan=2, pady=20)
