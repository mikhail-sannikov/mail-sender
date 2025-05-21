from settings import TEMPLATE_PATH


def get_message_body(template_name: str) -> str:
    with open(f'{TEMPLATE_PATH}{template_name}') as file:
        body = file.read()

    return body
