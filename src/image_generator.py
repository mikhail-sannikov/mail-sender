import os

from PIL import Image, ImageDraw, ImageFont

from settings import IMAGE_TEMPLATE_PATH, MEDIA


def generate_images_with_names(user_names: list[str]) -> list[str]:
    formatted_names = []

    for user_name in user_names:
        output_name = user_name.replace('\n', '').replace(' ', '_')

        add_name_to_template(user_name, output_name)
        formatted_names.append(output_name)

    return formatted_names


def add_name_to_template(user_name: str, output_name: str) -> None:
    img = Image.open(IMAGE_TEMPLATE_PATH)
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype('Jura-Bold.ttf', 45)
    except IOError:
        font = ImageFont.load_default()

    draw.text((45, 390), '\n'.join(user_name.upper().split()), fill=(255, 255, 255), font=font)

    output_path = os.path.join(MEDIA, f'{output_name}.png')
    img.save(output_path)
