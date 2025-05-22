import logging
from smtplib import SMTP_SSL, SMTPException
from tkinter import messagebox

from ttkbootstrap import Entry, Toplevel, Window

from apps.main.gui.windows import create_main_window
from consts import SMTPConsts

logger = logging.getLogger('smtp')


def login(root: Window, window: Toplevel, email_entry: Entry, password_entry: Entry) -> None:
    email = email_entry.get()
    password = password_entry.get()

    if not email or not password:
        messagebox.showerror('Ошибка', 'Заполните все поля!')
        return

    try:
        with SMTP_SSL(SMTPConsts.HOST.value, SMTPConsts.PORT.value) as client:
            logger.debug(f'Попытка авторизоваться на SMTP сервере почты {email}')
            client.login(email, password)
            logger.info(f'Авторизация на SMTP сервере почты {email} прошла успешно')
    except SMTPException:
        logger.info(f'Авторизация на SMTP сервере почты {email} не удалась')
        messagebox.showerror('Ошибка', 'Введены неверные данные от SMTP почты')
        return

    window.destroy()
    create_main_window(root, email, password)
