from getpass import getpass as gp

from src.image_generator import generate_images_with_names
from src.parsers import get_receivers
from src.smtp_server import send_emails


def main() -> None:
    sender_email = input('sender_email: ')
    password = gp('password: ')

    receivers = get_receivers()
    receivers_names = [receiver[0] for receiver in receivers]

    generate_images_with_names(receivers_names)
    send_emails(sender_email, password, receivers)


if __name__ == '__main__':
    main()
