def interval_mapper(note: str, interval: str) -> str:
    notes = {
        "A": ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"],
        "Bb": ["Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A"],
        "B": ["D", "D#", "E", "F", "F#", "G", "G#", "A", "A#"],
        "C": ["Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"],
        "C#": ["E", "F", "F#", "G", "G#", "A", "A#", "B", "C"],
        "D": ["F", "F#", "G", "Ab", "A", "Bb", "B", "C", "C#"],
        "Eb": ["F#", "G", "Ab", "A", "Bb", "B", "C", "Db", "D"],
        "E": ["G", "G#", "A", "A#", "B", "C", "C#", "D", "D#"],
        "F": ["Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E"],
        "F#": ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F"],
        "G": ["Bb", "B", "C", "C#", "D", "Eb", "E", "F", "F#"],
        "Ab": ["B", "C", "Db", "D", "Eb", "E", "F", "F#", "G"],
    }

    intervals = [
        "minor 3rd",
        "major 3rd",
        "perfect 4th",
        "tritone",
        "perfect 5th",
        "minor 6th",
        "major 6th",
        "minor 7th",
        "major 7th",
    ]

    return notes[note][intervals.index(interval)]
