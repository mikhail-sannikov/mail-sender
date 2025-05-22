def get_file_data(path: str) -> str:
    with open(path) as file:
        return file.read()
