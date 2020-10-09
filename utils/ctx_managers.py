from os import system
from contextlib import contextmanager


@contextmanager
def terminal_cleaner():
    system("clear")
    yield
    system("clear")
