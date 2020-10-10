from os import system
from time import sleep
from typing import Callable

from exercises.intervals import RandomInterval
from exercises.triads import TriadInversions
from exercises.major_modes import Modes
from utils.arg_parser import parse
from utils.ctx_managers import terminal_cleaner


def run(func: Callable, wait: int = 5) -> None:
    question, answer = func()
    system("clear")
    with terminal_cleaner():
        print(question)
        sleep(wait)
    print(answer)
    sleep(2)


if __name__ == "__main__":
    args = parse()
    exercises = {
        "triads": TriadInversions(args.triad),
        "intervals": RandomInterval(),
        "modes": Modes(args.mode),
    }
    while True:
        run(exercises[args.exercise])
