from getpass import getpass as gp

from src.handlers import peek_message_template
from src.image_generator import generate_images_with_names
from src.parsers import get_receivers
from src.smtp_server import send_emails


def main() -> None:
    sender_email = input('sender_email: ')
    password = gp('password: ')

    message_body_template_name = peek_message_template()

    receivers = get_receivers()

    receivers_names = [receiver[0] for receiver in receivers]
    receivers_emails = [receiver[1] for receiver in receivers]

    formatted_names = generate_images_with_names(receivers_names)

    send_emails(sender_email, password, formatted_names, receivers_emails, message_body_template_name)


if __name__ == '__main__':
    main()
