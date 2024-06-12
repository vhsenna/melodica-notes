from pytest import mark

from melodica_notes.chords import chord


@mark.parametrize(
    "tonic_note, expected",
    [
        ("C", ["C", "E", "G"]),
        ("Cm", ["C", "D#", "G"]),
        ("Cdim", ["C", "D#", "F#"]),
        ("C+", ["C", "E", "G#"]),
        ("Cm+", ["C", "D#", "G#"]),

        ("F#", ["F#", "A#", "C#"]),
        ("F#m", ["F#", "A", "C#"]),
        ("F#dim", ["F#", "A", "C"]),
        ("F#+", ["F#", "A#", "D"]),
        ("F#m+", ["F#", "A", "D"]),

        ("Gb", ["Gb", "Bb", "Db"]),
        ("Gbm", ["Gb", "A", "Db"]),
        ("Gbdim", ["Gb", "A", "C"]),
        ("Gb+", ["Gb", "Bb", "D"]),
        ("Gbm+", ["Gb", "A", "D"]),
    ]
)
def test_chords_return_corresponding_notes(tonic_note, expected):
    notes, _ = chord(tonic_note).values()
    assert expected == notes


@mark.parametrize(
    "tonic_note, expected",
    [
        ("C", ["I", "III", "V"]),
        ("Cm", ["I", "III-", "V"]),
        ("Cdim", ["I", "III-", "V-"]),
        ("C+", ["I", "III", "V+"]),
        ("Cm+", ["I", "III-", "V+"]),
    ]
)
def test_chords_return_corresponding_degrees(tonic_note, expected):
    _, degrees = chord(tonic_note).values()
    assert expected == degrees
