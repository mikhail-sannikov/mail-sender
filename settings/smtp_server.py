import os

SMTP_HOST = os.getenv('SMTP_HOST', 'smtp.mail.ru')
SMTP_PORT = os.getenv('SMTP_PORT', 465)
