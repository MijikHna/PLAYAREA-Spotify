import random

# TODO: make it the right way


def generate_random_string(length: int) -> str:
    text: str = ''
    possible: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

    for i in range(length):
        text += possible[random.randint(0, len(possible) - 1)]
    return text
