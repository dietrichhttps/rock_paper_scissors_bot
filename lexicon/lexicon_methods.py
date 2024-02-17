import os


def get_text(module_path: str, text_path: str) -> str:

    absolute_path = os.path.join(module_path, text_path)

    with open(absolute_path, 'r') as f:
        text = f.read()

    return text
