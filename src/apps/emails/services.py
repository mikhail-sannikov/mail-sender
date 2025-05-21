from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from infrastructure.smtp import SMTPClient


def send_emails(client: SMTPClient, emails: list[str], message_body: str) -> None:
    for receiver_email in emails:
        send_email(client, receiver_email, message_body)


def send_email(client: SMTPClient, receiver_email: str, message_body: str) -> None:
    message = MIMEMultipart('alternative')

    message['Subject'] = ''  # TODO какой Subject?
    message['From'] = client.email
    message['To'] = receiver_email

    message.attach(MIMEText(message_body, 'html'))

    with client as client:
        client.sendmail(client.email, receiver_email, message.as_string())
