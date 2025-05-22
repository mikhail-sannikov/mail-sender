from consts import PathConsts

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] [%(levelname)s] %(module)s : %(message)s',
            'datefmt': '%d.%m.%Y %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'stream': 'ext://sys.stdout',
        },
        'smtp_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': PathConsts.LOGS_PATH.value / 'smtp.log',
        },
    },
    'loggers': {
        'smtp': {
            'level': 'DEBUG',
            'handlers': ['console', 'smtp_file'],
            'propagate': False,
        },
    },
}
