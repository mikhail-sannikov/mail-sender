def get_message_body() -> str:
    with open('templates/message_body.html') as file:
        body = file.read()

    return body
