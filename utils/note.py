from dataclasses import dataclass
from operator import iadd, isub

from data.notes import CIRCLE_OF_FIFTH_NOTES


@dataclass
class Note:
    note: str

    def flat(self):
        return self._change_by_half_step(isub)

    def sharp(self):
        return self._change_by_half_step(iadd)

    def _change_by_half_step(self, operator):
        notes = CIRCLE_OF_FIFTH_NOTES
        index = notes.index(self.note)
        index = operator(index, 1)

        if index == len(notes):
            index = 0
        elif index == -1:
            index = len(notes) - 1

        self.note = notes[index]
        return self
