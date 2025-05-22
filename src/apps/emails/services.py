import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL, SMTPException
from typing import Any

from consts import SMTPConsts

logger = logging.getLogger('smtp')


class EmailService:
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password

    def send_emails(self, emails: list[str], message_body: str) -> None:
        for receiver_email in emails:
            self._send_email(receiver_email, message_body)

    def _send_email(self, receiver_email: str, message_body: str) -> None:
        message = self._attach_message(receiver_email, message_body)

        with SMTP_SSL(SMTPConsts.HOST.value, SMTPConsts.PORT.value) as client:
            client.login(self.email, self.password)
            logger.debug(f'Попытка отправить письмо на {receiver_email}')
            try:
                client.sendmail(self.email, receiver_email, message.as_string())
                logger.info(f'Письмо на почту {receiver_email} успешно отправлено')
            except SMTPException:
                logger.info(f'Письмо на почту {receiver_email} не было доставлено')

    def _attach_message(self, receiver_email: str, message_body: str) -> Any:
        message = MIMEMultipart('alternative')

        message['Subject'] = 'Рассылка'
        message['From'] = self.email
        message['To'] = receiver_email

        message.attach(MIMEText(message_body, 'html'))

        return message
