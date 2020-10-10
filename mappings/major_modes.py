from copy import deepcopy
from random import choice
from typing import List, Tuple

from utils.note import Note


LYDIAN = {
    "C": ["C", "D", "E", "F#", "G", "A", "B"],
    "F": ["F", "G", "A", "B", "C", "D", "E"],
    "Bb": ["Bb", "C", "D", "E", "F", "G", "A"],
    "Eb": ["Eb", "F", "G", "A", "Bb", "C", "D"],
    "Ab": ["Ab", "Bb", "C", "D", "Eb", "F", "G"],
    "Db": ["Db", "Eb", "F", "G", "Ab", "Bb", "C"],
    "F#": ["F#", "Ab", "Bb", "C", "Db", "Eb", "F"],
    "B": ["B", "Db", "Eb", "F", "F#", "Ab", "Bb"],
    "E": ["E", "F#", "Ab", "Bb", "B", "Db", "Eb"],
    "A": ["A", "B", "Db", "Eb", "E", "F#", "Ab"],
    "D": ["D", "E", "F#", "Ab", "A", "B", "Db"],
    "G": ["G", "A", "B", "Db", "D", "E", "F#"],
}


def _lower(lydian: List[str], position: int) -> List[str]:
    copy = deepcopy(lydian)
    copy[position] = Note(copy[position]).flat().note
    return copy


def ionian(lydian: List[str]) -> List[str]:
    return _lower(lydian, 3)


def mixolydian(lydian: List[str]) -> List[str]:
    return _lower(ionian(lydian), 6)


def dorian(lydian: List[str]) -> List[str]:
    return _lower(mixolydian(lydian), 2)


def aeolian(lydian: List[str]) -> List[str]:
    return _lower(dorian(lydian), 5)


def phrygian(lydian: List[str]) -> List[str]:
    return _lower(aeolian(lydian), 1)


def locrian(lydian: List[str]) -> List[str]:
    return _lower(phrygian(lydian), 4)


IONIAN = {note: ionian(scale) for note, scale in LYDIAN.items()}
DORIAN = {note: dorian(scale) for note, scale in LYDIAN.items()}
PHRYGIAN = {note: phrygian(scale) for note, scale in LYDIAN.items()}
MIXOLYDIAN = {note: mixolydian(scale) for note, scale in LYDIAN.items()}
AEOLIAN = {note: aeolian(scale) for note, scale in LYDIAN.items()}
LOCRIAN = {note: locrian(scale) for note, scale in LYDIAN.items()}


def mode_mapper(root: str, mode_type: str) -> Tuple[List[str], str]:
    switch = {
        "ionian": IONIAN,
        "dorian": DORIAN,
        "phrygian": PHRYGIAN,
        "lydian": LYDIAN,
        "mixolydian": MIXOLYDIAN,
        "aeolian": AEOLIAN,
        "locrian": LOCRIAN,
    }

    if mode_type == "all":
        mode_type = choice(list(switch.keys()))

    mode = switch[mode_type]

    return mode[root], mode_type
