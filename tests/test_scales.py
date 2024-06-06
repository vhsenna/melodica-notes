from pytest import mark, raises

from melodica_notes.scales import NOTES, SCALES, scale


def test_handles_lowercase_notes():
    tonic_note = "c"
    scale_mode = "major"

    result = scale(tonic_note, scale_mode)
    assert result


def test_raises_error_for_invalid_note():
    tonic_note = "X"
    scale_mode = "major"

    error_message = (
        f"This tonic note does not exist. Please use one of these: {NOTES}")

    with raises(ValueError) as error:
        scale(tonic_note, scale_mode)
        assert error_message == error.value.args[0]


def test_raises_error_for_invalid_scale_mode():
    tonic_note = "C"
    scale_mode = "scale"

    error_message = ("This scale mode does not exist or has not been implemented. Please use one of these: "
                     f"{list(SCALES.keys())}")

    with raises(KeyError) as error:
        scale(tonic_note, scale_mode)
        assert error_message == error.value.args[0]


@mark.parametrize(
    'tonic_note, scale_mode, expected',
    [
        # Major Scales
        ('C', 'major', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', 'major', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('D', 'major', ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']),
        ('D#', 'major', ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D']),
        ('E', 'major', ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#']),
        ('F', 'major', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
        ('F#', 'major', ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F']),
        ('G', 'major', ['G', 'A', 'B', 'C', 'D', 'E', 'F#']),
        ('G#', 'major', ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G']),
        ('A', 'major', ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']),
        ('A#', 'major', ['A#', 'C', 'D', 'D#', 'F', 'G', 'A']),
        ('B', 'major', ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']),

        # Minor Scales
        ('C', 'minor', ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']),
        ('C#', 'minor', ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']),
        ('D', 'minor', ['D', 'E', 'F', 'G', 'A', 'A#', 'C']),
        ('D#', 'minor', ['D#', 'F', 'F#', 'G#', 'A#', 'B', 'C#']),
        ('E', 'minor', ['E', 'F#', 'G', 'A', 'B', 'C', 'D']),
        ('F', 'minor', ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#']),
        ('F#', 'minor', ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E']),
        ('G', 'minor', ['G', 'A', 'A#', 'C', 'D', 'D#', 'F']),
        ('G#', 'minor', ['G#', 'A#', 'B', 'C#', 'D#', 'E', 'F#']),
        ('A', 'minor', ['A', 'B', 'C', 'D', 'E', 'F', 'G']),
        ('A#', 'minor', ['A#', 'C', 'C#', 'D#', 'F', 'F#', 'G#']),
        ('B', 'minor', ['B', 'C#', 'D', 'E', 'F#', 'G', 'A']),
    ],
)
def test_should_return_correct_scale_notes(tonic_note, scale_mode, expected):
    result = scale(tonic_note, scale_mode)
    assert result['notes'] == expected


def test_should_return_seven_diatonic_degrees():
    tonic_note = 'C'
    scale_mode = 'major'
    expected = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

    result = scale(tonic_note, scale_mode)
    assert result['degrees'] == expected
