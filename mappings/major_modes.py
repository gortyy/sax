from random import choice
from typing import List, Tuple


IONIAN = {
    "C": ["C", "D", "E", "F", "G", "A", "B"],
    "F": ["F", "G", "A", "Bb", "C", "D", "E"],
    "Bb": ["Bb", "C", "D", "Eb", "F", "G", "A"],
    "Eb": ["Eb", "F", "G", "Ab", "Bb", "C", "D"],
    "Ab": ["Ab", "Bb", "C", "Db", "Eb", "F", "G"],
    "Db": ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"],
    "F#": ["F#", "G#", "A#", "B", "C#", "D#", "F"],
    "B": ["B", "C#", "D#", "E", "F#", "G#", "A#"],
    "E": ["E", "F#", "G#", "A", "B", "C#", "D#"],
    "A": ["A", "B", "C#", "D", "E", "F#", "G#"],
    "D": ["D", "E", "F#", "G", "A", "B", "C#"],
    "G": ["G", "A", "B", "C", "D", "E", "F#"],
}

DORIAN = {
    "C": ["C", "D", "Eb", "F", "G", "A", "Bb"],
    "F": ["F", "G", "Ab", "Bb", "C", "D", "Eb"],
    "Bb": ["Bb", "C", "Db", "Eb", "F", "G", "Ab"],
    "Eb": ["Eb", "F", "Gb", "Ab", "Bb", "C", "Db"],
    "Ab": ["Ab", "Bb", "B", "Db", "Eb", "F", "Gb"],
    "Db": ["Db", "Eb", "E", "Gb", "Ab", "Bb", "B"],
    "F#": ["F#", "G#", "A", "B", "C#", "D#", "E"],
    "B": ["B", "C#", "D", "E", "F#", "G#", "A"],
    "E": ["E", "F#", "G", "A", "B", "C#", "D"],
    "A": ["A", "B", "C", "D", "E", "F#", "G"],
    "D": ["D", "E", "F", "G", "A", "B", "C"],
    "G": ["G", "A", "Bb", "C", "D", "E", "F"],
}

PHRYGIAN = {
    "C": ["C", "Db", "Eb", "F", "G", "Ab", "Bb"],
    "F": ["F", "Gb", "Ab", "Bb", "C", "Db", "Eb"],
    "Bb": ["Bb", "B", "Db", "Eb", "F", "Gb", "Ab"],
    "Eb": ["Eb", "E", "Gb", "Ab", "Bb", "B", "Db"],
    "Ab": ["Ab", "A", "B", "Db", "Eb", "E", "Gb"],
    "Db": ["Db", "D", "E", "Gb", "Ab", "A", "B"],
    "F#": ["F#", "G", "A", "B", "C#", "D", "E"],
    "B": ["B", "C", "D", "E", "F#", "G", "A"],
    "E": ["E", "F", "G", "A", "B", "C", "D"],
    "A": ["A", "Bb", "C", "D", "E", "F", "G"],
    "D": ["D", "Eb", "F", "G", "A", "Bb", "C"],
    "G": ["G", "Ab", "Bb", "C", "D", "Eb", "F"],
}

LYDIAN = {
    "C": ["C", "D", "E", "F#", "G", "A", "B"],
    "F": ["F", "G", "A", "B", "C", "D", "E"],
    "Bb": ["Bb", "C", "D", "E", "F", "G", "A"],
    "Eb": ["Eb", "F", "G", "A", "Bb", "C", "D"],
    "Ab": ["Ab", "Bb", "C", "D", "Eb", "F", "G"],
    "Db": ["Db", "Eb", "F", "G", "Ab", "Bb", "C"],
    "F#": ["F#", "G#", "A#", "C", "C#", "D#", "F"],
    "B": ["B", "C#", "D#", "F", "F#", "G#", "A#"],
    "E": ["E", "F#", "G#", "A#", "B", "C#", "D#"],
    "A": ["A", "B", "C#", "D#", "E", "F#", "G#"],
    "D": ["D", "E", "F#", "G#", "A", "B", "C#"],
    "G": ["G", "A", "B", "C#", "D", "E", "F#"],
}

MIXOLYDIAN = {
    "C": ["C", "D", "E", "F", "G", "A", "Bb"],
    "F": ["F", "G", "A", "Bb", "C", "D", "Eb"],
    "Bb": ["Bb", "C", "D", "Eb", "F", "G", "Ab"],
    "Eb": ["Eb", "F", "G", "Ab", "Bb", "C", "Db"],
    "Ab": ["Ab", "Bb", "C", "Db", "Eb", "F", "Gb"],
    "Db": ["Db", "Eb", "F", "Gb", "Ab", "Bb", "B"],
    "F#": ["F#", "G#", "A#", "B", "C#", "D#", "E"],
    "B": ["B", "C#", "D#", "E", "F#", "G#", "A"],
    "E": ["E", "F#", "G#", "A", "B", "C#", "D"],
    "A": ["A", "B", "C#", "D", "E", "F#", "G"],
    "D": ["D", "E", "F#", "G", "A", "B", "C"],
    "G": ["G", "A", "B", "C", "D", "E", "F"],
}

AEOLIAN = {
    "C": ["C", "D", "Eb", "F", "G", "Ab", "Bb"],
    "F": ["F", "G", "Ab", "Bb", "C", "Db", "Eb"],
    "Bb": ["Bb", "C", "Db", "Eb", "F", "Gb", "Ab"],
    "Eb": ["Eb", "F", "Gb", "Ab", "Bb", "B", "Db"],
    "Ab": ["Ab", "Bb", "B", "Db", "Eb", "E", "Gb"],
    "Db": ["Db", "Eb", "E", "Gb", "Ab", "A", "B"],
    "F#": ["F#", "G#", "A", "B", "C#", "D", "E"],
    "B": ["B", "C#", "D", "E", "F#", "G", "A"],
    "E": ["E", "F#", "G", "A", "B", "C", "D"],
    "A": ["A", "B", "C", "D", "E", "F", "G"],
    "D": ["D", "E", "F", "G", "A", "Bb", "C"],
    "G": ["G", "A", "Bb", "C", "D", "Eb", "F"],
}

LOCRIAN = {
    "C": ["C", "Db", "Eb", "F", "Gb", "Ab", "Bb"],
    "F": ["F", "Gb", "Ab", "Bb", "B", "Db", "Eb"],
    "Bb": ["Bb", "B", "Db", "Eb", "E", "Gb", "Ab"],
    "Eb": ["Eb", "E", "Gb", "Ab", "A", "B", "Db"],
    "Ab": ["Ab", "A", "B", "Db", "D", "E", "Gb"],
    "Db": ["Db", "D", "E", "Gb", "G", "A", "B"],
    "F#": ["F#", "G", "A", "B", "C", "D", "E"],
    "B": ["B", "C", "D", "E", "F", "G", "A"],
    "E": ["E", "F", "G", "A", "Bb", "C", "D"],
    "A": ["A", "Bb", "C", "D", "Eb", "F", "G"],
    "D": ["D", "Eb", "F", "G", "Ab", "Bb", "C"],
    "G": ["G", "Ab", "Bb", "C", "Db", "Eb", "F"],
}


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
