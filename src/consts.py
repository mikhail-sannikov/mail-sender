from enum import Enum
from pathlib import Path

from config.env import env


class PathConsts(Enum):
    PROJECT_ROOT = Path(__file__).parent.parent
    LOGS_PATH = PROJECT_ROOT / 'logs'


class SMTPConsts(Enum):
    HOST = env.str('SMTP_HOST', 'smtp.mail.ru')
    PORT = env.int('SMTP_PORT', 465)
