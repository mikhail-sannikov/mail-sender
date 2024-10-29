from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL, SMTPException
from typing import ByteString

import settings
from src.parsers import get_image_data, get_message_body


def send_emails(
    sender_email: str, password: str, names: list[str], emails: list[str], message_body_template_name: str
) -> None:
    for receiver_name, receiver_email in zip(names, emails, strict=False):
        message_body = get_message_body(message_body_template_name)
        image_path = settings.MEDIA + f'{"_".join(receiver_name.split())}.png'
        image_data = get_image_data(image_path)

        send_email(sender_email, password, receiver_email, message_body, image_data)


def send_email(
    sender_email: str, password: str, receiver_email: str, message_body: str, image_data: ByteString
) -> None:
    message = MIMEMultipart('alternative')

    message['Subject'] = 'MEETUP ITCODE'
    message['From'] = sender_email
    message['To'] = receiver_email

    message.attach(MIMEText(message_body, 'html'))
    mime_image = MIMEImage(image_data)
    mime_image.add_header('Content-Disposition', 'inline', filename='invite.png')
    message.attach(mime_image)

    try:
        with SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            settings.smtp_logger.debug(f'Попытка авторизоваться на SMTP сервере почты {sender_email}')
            server.login(sender_email, password)
            settings.smtp_logger.debug(f'Авторизация {sender_email} прошла успешно')

            server.sendmail(sender_email, receiver_email, message.as_string())
            settings.smtp_logger.debug(f'{sender_email} отправил письмо {receiver_email}')
    except SMTPException as e:
        settings.smtp_logger.error(f'Ошибка при отправке письма: {e}')
