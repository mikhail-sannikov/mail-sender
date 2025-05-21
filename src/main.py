import logging.config

import ttkbootstrap as ttk

from apps.auth.gui.windows import create_login_window
from loggers.config import LOGGING_CONFIG


def main() -> None:
    logging.config.dictConfig(LOGGING_CONFIG)
    start_gui_app()


def start_gui_app() -> None:
    root = ttk.Window(themename='superhero')
    root.withdraw()

    create_login_window(root)
    root.mainloop()


if __name__ == '__main__':
    main()
