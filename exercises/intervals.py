from random import choice

from exercises import Answer, Question
from data.notes import CIRCLE_OF_FIFTH_NOTES
from data.intervals import INTERVALS
from mappings.intervals import interval_mapper


class RandomInterval:
    def __call__(self) -> tuple[Question, Answer]:
        note, interval = (
            choice(CIRCLE_OF_FIFTH_NOTES),
            choice(list(INTERVALS.keys())),
        )
        answer = interval_mapper(note, interval)

        return f"{note} {interval}", answer
