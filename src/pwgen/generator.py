import string
import random


letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

choices = [letters, numbers, symbols]

DEFAULT_PASSWORD_LENGTH = 10

def gen(length: int = None) -> str:
    """
    Generates a random string of length `length`.
    :param length: the length of the string to generate
    :return: the string as combination of the values of several arrays
    """
    password_length = DEFAULT_PASSWORD_LENGTH if length is None else length
    password = ""
    for threshold in range(0, password_length):
        choice = choices[random.randint(0, len(choices) - 1)]
        password += random.choice(choice)

    return password



