import logging
from smtplib import SMTP_SSL, SMTPException
from types import TracebackType
from typing import Type


class SMTPClient(SMTP_SSL):
    def __init__(self, email: str, password: str, logger: str = 'smtp', *args: tuple, **kwargs: dict) -> None:
        self.email = email
        self.password = password

        self._logger = logging.getLogger(logger)

        super().__init__(*args, **kwargs)

    def __enter__(self) -> 'SMTPClient':
        self._logger.debug(f'Попытка авторизоваться на SMTP сервере почты {self.email}')
        self.login(self.email, self.password)
        self._logger.debug(f'Авторизация {self.email} прошла успешно')
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: Type[BaseException] | None,
        exc_tb: Type[TracebackType] | None,
    ) -> None:
        try:
            super().__exit__(exc_type, exc_val, exc_tb)
        except SMTPException as e:
            self._logger.error(f'Ошибка при отправке письма: {e}')
