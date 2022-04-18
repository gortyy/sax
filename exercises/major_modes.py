from random import choice

from exercises import Answer, Question
from data.notes import CIRCLE_OF_FIFTH_NOTES
from data.major_modes import MODES
from mappings.major_modes import mode_mapper


class Modes:
    def __init__(self, mode_type: str):
        self.mode_type = mode_type

    def __call__(self) -> tuple[Question, Answer]:
        root = choice(CIRCLE_OF_FIFTH_NOTES)
        notes, mode_type = mode_mapper(root, self.mode_type)

        return (f"{root} {mode_type}", notes)
