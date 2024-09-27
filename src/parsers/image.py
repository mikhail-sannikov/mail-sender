from typing import ByteString


def get_image_data(path: str) -> ByteString:
    with open(path, 'rb') as file:
        data = file.read()

    return data
