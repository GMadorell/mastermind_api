import random


def remove_random_char(string: str)-> str:
    index = random.randint(0, len(string) - 1)
    return string[:index] + string[index + 1:]
