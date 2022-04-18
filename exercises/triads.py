from enum import Enum
from dataclasses import dataclass
from random import choice

from exercises import Answer, Question
from data.notes import CIRCLE_OF_FIFTH_NOTES


class TriadType(str, Enum):
    MAJOR = "major"
    MINOR = "minor"
    DIMINISHED = "diminished"
    AUGMENTED = "augmented"


class Inversion(str, Enum):
    ROOT = "root"
    FIRST = "first inversion"
    SECOND = "second inversion"


@dataclass
class Triad:
    root: str
    type: TriadType
    inversion: Inversion

    def mapper(self) -> tuple[list[str], str]:
        inversions = {
            Inversion.ROOT: lambda triad: triad,
            Inversion.FIRST: lambda triad: triad[1:] + [triad[0]],
            Inversion.SECOND: lambda triad: [triad[2]] + triad[:2],
        }

        switch = {
            TriadType.MAJOR: MAJOR,
            TriadType.MINOR: MINOR,
            TriadType.DIMINISHED: DIMINISHED,
            TriadType.AUGMENTED: AUGMENTED,
        }

        triad_type = (
            self.type if self.type is not None else choice(t for t in TriadType)
        )

        triads = switch[triad_type]

        return inversions[self.inversion](triads[self.root]), triad_type


class TriadInversions:
    def __init__(self, triad_type: TriadType):
        # TODO Fix
        self.triad_type = TriadType(triad_type)

    def __call__(self) -> tuple[Question, Answer]:
        root, inversion = (
            choice(CIRCLE_OF_FIFTH_NOTES),
            choice([i for i in Inversion]),
        )
        triad = Triad(root, self.triad_type, inversion)
        notes, triad_type = triad.mapper()

        return f"{root} {triad_type} {inversion}", notes


MAJOR = {
    "C": ["C", "E", "G"],
    "F": ["F", "A", "C"],
    "Bb": ["Bb", "D", "F"],
    "Eb": ["Eb", "G", "Bb"],
    "Ab": ["Ab", "C", "Eb"],
    "Db": ["Db", "F", "Ab"],
    "F#": ["F#", "A#", "C#"],
    "B": ["B", "D#", "F#"],
    "E": ["E", "G#", "B"],
    "A": ["A", "C#", "E"],
    "D": ["D", "F#", "A"],
    "G": ["G", "B", "D"],
}
MINOR = {
    "C": ["C", "Eb", "G"],
    "F": ["F", "Ab", "C"],
    "Bb": ["Bb", "Db", "F"],
    "Eb": ["Eb", "Gb", "Bb"],
    "Ab": ["Ab", "B", "Eb"],
    "Db": ["Db", "E", "Ab"],
    "F#": ["F#", "A", "C#"],
    "B": ["B", "D", "F#"],
    "E": ["E", "G", "B"],
    "A": ["A", "C", "E"],
    "D": ["D", "F", "A"],
    "G": ["G", "Bb", "D"],
}
DIMINISHED = {
    "C": ["C", "Eb", "Gb"],
    "F": ["F", "Ab", "B"],
    "Bb": ["Bb", "Db", "E"],
    "Eb": ["Eb", "Gb", "A"],
    "Ab": ["Ab", "B", "D"],
    "Db": ["Db", "E", "G"],
    "F#": ["F#", "A", "C"],
    "B": ["B", "D", "F"],
    "E": ["E", "G", "Bb"],
    "A": ["A", "C", "Eb"],
    "D": ["D", "F", "Ab"],
    "G": ["G", "Bb", "Db"],
}
AUGMENTED = {
    "C": ["C", "E", "G#"],
    "F": ["F", "A", "C#"],
    "Bb": ["Bb", "D", "F#"],
    "Eb": ["Eb", "G", "B"],
    "Ab": ["Ab", "C", "E"],
    "Db": ["Db", "F", "A"],
    "F#": ["F#", "A#", "D"],
    "B": ["B", "D#", "G"],
    "E": ["E", "G#", "C"],
    "A": ["A", "C#", "F"],
    "D": ["D", "F#", "A#"],
    "G": ["G", "B", "D#"],
}
