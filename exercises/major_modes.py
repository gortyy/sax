from random import choice
from functools import partial
from typing import Tuple

from exercises import Exercise
from exercises.types import Question, Answer
from data.notes import ALL_NOTES, CIRCLE_OF_FIFTH_NOTES
from data.major_modes import MODES
from mappings.major_modes import mode_mapper


class Modes(Exercise):
    def __init__(self, mode_type: str):
        self.mode_type = mode_type

    def __call__(self) -> Tuple[Question, Answer]:
        root = choice(CIRCLE_OF_FIFTH_NOTES)
        mapper = partial(mode_mapper, mode_type=self.mode_type)
        notes, mode_type = mapper(root)
        answer = "".join([ALL_NOTES[note] for note in notes])

        return (
            f"{ALL_NOTES[root]}{MODES[mode_type]}",
            answer,
        )
