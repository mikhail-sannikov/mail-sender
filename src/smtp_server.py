from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL, SMTPException
from typing import ByteString

import settings
from src.parsers import get_image_data, get_message_body


def send_emails(receivers: list[tuple]) -> None:
    for receiver_name, receiver_email in receivers:
        message_body = get_message_body()
        image_path = settings.MEDIA + f'{"_".join(receiver_name.split())}.png'
        image_data = get_image_data(image_path)

        send_email(receiver_email, message_body, image_data)


def send_email(receiver_email: str, message_body: str, image_data: ByteString) -> None:
    message = MIMEMultipart('alternative')

    message['Subject'] = 'MEETUP ITCODE'
    message['From'] = settings.SENDER_EMAIL
    message['To'] = receiver_email

    message.attach(MIMEText(message_body, 'html'))
    message.attach(MIMEImage(image_data))

    try:
        with SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            settings.smtp_logger.debug(f'Попытка авторизоваться на SMTP сервере почты {settings.SENDER_EMAIL}')
            server.login(settings.SENDER_EMAIL, settings.SENDER_PASSWORD)
            settings.smtp_logger.debug(f'Авторизация {settings.SENDER_EMAIL} прошла успешно')

            server.sendmail(settings.SENDER_EMAIL, receiver_email, message.as_string())
            settings.smtp_logger.debug(f'{settings.SENDER_EMAIL} отправил письмо {receiver_email}')
    except SMTPException as e:
        settings.smtp_logger.error(f'Ошибка при отправке письма: {e}')
