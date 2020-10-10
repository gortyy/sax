from random import choice
from typing import List, Tuple

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


def triad_mapper(
    root: str, inversion: int, triad_type: str
) -> Tuple[List[str], str]:
    inversions = {
        1: lambda triad: triad,
        2: lambda triad: triad[1:] + [triad[0]],
        3: lambda triad: [triad[2]] + triad[:2],
    }

    switch = {
        "major": MAJOR,
        "minor": MINOR,
        "diminished": DIMINISHED,
        "augmented": AUGMENTED,
    }

    if triad_type == "all":
        triad_type = choice(list(switch.keys()))
    triads = switch[triad_type]

    return inversions[inversion](triads[root]), triad_type
