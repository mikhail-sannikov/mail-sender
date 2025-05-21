from enum import Enum
from pathlib import Path


class PathConsts(Enum):
    PROJECT_ROOT = Path(__file__).parent.parent
    LOGS_PATH = PROJECT_ROOT / 'logs'
