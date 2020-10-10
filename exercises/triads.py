from random import choice
from functools import partial
from typing import Tuple

from exercises import Exercise
from exercises.types import Question, Answer
from data.notes import ALL_NOTES, CIRCLE_OF_FIFTH_NOTES
from data.triads import INVERSIONS, TYPE
from mappings.triads import triad_mapper


class TriadInversions(Exercise):
    def __init__(self, triad_type: str):
        self.triad_type = triad_type

    def __call__(self) -> Tuple[Question, Answer]:
        root, inversion = (
            choice(CIRCLE_OF_FIFTH_NOTES),
            choice(list(INVERSIONS.keys())),
        )
        mapper = partial(triad_mapper, triad_type=self.triad_type)
        notes, triad_type = mapper(root, inversion)
        answer = "".join([ALL_NOTES[note] for note in notes])

        return (
            f"{ALL_NOTES[root]}{TYPE[triad_type]}{INVERSIONS[inversion]}",
            answer,
        )
