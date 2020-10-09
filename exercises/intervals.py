from random import choice
from typing import Tuple

from exercises import Exercise
from exercises.types import Question, Answer
from data.notes import ALL_NOTES, CIRCLE_OF_FIFTH_NOTES
from data.intervals import INTERVALS
from mappings.intervals import interval_mapper


class RandomInterval(Exercise):
    def __call__(self) -> Tuple[Question, Answer]:
        note, interval = (
            choice(CIRCLE_OF_FIFTH_NOTES),
            choice(list(INTERVALS.keys())),
        )
        answer = ALL_NOTES[interval_mapper(note, interval)]

        return f"{ALL_NOTES[note]}{INTERVALS[interval]}", answer
