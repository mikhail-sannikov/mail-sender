from pathlib import Path
from tkinter import StringVar, filedialog, messagebox

import pandas as pd


def choose_emails_file(emails_file_path: StringVar) -> None:
    file_path = filedialog.askopenfilename(
        filetypes=[('Excel files', '*.xlsx *.xls'), ('All files', '*.*')], title='Выберите файл с почтами (Excel)'
    )
    if file_path:
        try:  # TODO вынести в services
            pd.read_excel(file_path)
            emails_file_path.set(file_path)
        except Exception as e:
            messagebox.showerror('Ошибка', f'Не удалось прочитать файл: {str(e)}')


def choose_html_file(html_file_path: StringVar) -> None:
    file_path = filedialog.askopenfilename(
        filetypes=[('HTML files', '*.html *.htm'), ('All files', '*.*')], title='Выберите HTML файл письма'
    )
    if file_path:
        try:  # TODO вынести в services
            with open(file_path, 'r', encoding='utf-8') as f:
                f.read()
            html_file_path.set(file_path)
        except Exception as e:
            messagebox.showerror('Ошибка', f'Не удалось прочитать файл: {str(e)}')


def send(emails_file_path: StringVar, html_file_path: StringVar, sender_email: str) -> None:
    if emails_file_path.get() == 'Файл с почтами не выбран':
        messagebox.showerror('Ошибка', 'Выберите файл с почтами!')
        return

    if html_file_path.get() == 'HTML файл не выбран':
        messagebox.showerror('Ошибка', 'Выберите HTML файл письма!')
        return

    try:  # TODO вынести в services
        df = pd.read_excel(emails_file_path.get())
        if 'email' not in df.columns:
            messagebox.showerror('Ошибка', 'Файл должен содержать столбец "email"!')
            return

        emails = df['email'].tolist()

        with open(html_file_path.get(), 'r', encoding='utf-8') as f:
            html_content = f.read()  # noqa

        # TODO логика отправки

        messagebox.showinfo(
            'Успех',
            f'Готово к отправке!\n'
            f'Писем: {len(emails)}\n'
            f'От: {sender_email}\n'
            f'HTML файл: {Path(html_file_path.get()).name}',
        )

    except Exception as e:
        messagebox.showerror('Ошибка', f'Не удалось отправить письма: {str(e)}')
