import logging

smtp_logger = logging.getLogger('smtp')
smtp_logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logs/smtp.log')
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

smtp_logger.addHandler(file_handler)
smtp_logger.addHandler(console_handler)
