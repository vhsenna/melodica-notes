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
