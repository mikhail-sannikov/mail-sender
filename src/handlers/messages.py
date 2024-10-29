from os import listdir

from settings import TEMPLATE_PATH


def peek_message_template() -> str:
    available_names = filter(lambda file: file.split('.')[-1] == 'html', listdir(TEMPLATE_PATH))
    variants = {num: name for num, name in enumerate(available_names, 1)}

    max_file_name_length = len(max(variants.values(), key=lambda file_name: len(file_name))) + 3

    print('\nВыберите шаблон для текста сообщения:')
    print('-' * max_file_name_length)

    for key, value in variants.items():
        print(f'{key}: {value}')

    print('-' * max_file_name_length, end='\n\n')

    choice = int(input('message_body_template_name: '))

    if choice not in variants:
        raise ValueError('Не существует указанного шаблона!')

    template_name = variants[choice]

    return template_name
