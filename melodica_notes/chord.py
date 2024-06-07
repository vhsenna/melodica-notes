from melodica_notes.scale import NOTES, scale


def _minor(tonic_note: str) -> tuple[list[str], list[str]]:
    """
    Generates the minor triad based on the given tonic note.

    Args:
        tonic_note (str): The tonic note representing the root of the minor
            triad.

    Returns:
        tuple[list[str], list[str]]: A tuple containing the notes and degrees
            of the minor triad.

    Examples:
        >>> _minor("Cm")
        (['C', 'D#', 'G'], ['I', 'III-', 'V'])

        >>> _minor("Cm+")
        (['C', 'D#', 'G#'], ['I', 'III-', 'V+'])
    """
    key, _ = tonic_note.split("m")

    if "+" in tonic_note:
        tonic, third, fifth = _triad(key, "minor")
        keys = [tonic, third, _semitone(fifth, interval=1)]
        degrees = ["I", "III-", "V+"]
    else:
        keys = _triad(key, "minor")
        degrees = ["I", "III-", "V"]

    return keys, degrees


def _semitone(tonic_note: str, *, interval: int) -> str:
    """
    Returns the note that is a semitone away from the given tonic note.

    Args:
        tonic_note (str): The starting note or key.
        interval (int): The number of semitones to move from the tonic note.
            Positive values move upward, and negative values move downward.

    Returns:
        str: The note that is a semitone away from the tonic note.

    Examples:
        >>> _semitone('C', interval=1)
        'C#'
        >>> _semitone('A', interval=-1)
        'G#'
    """
    position = NOTES.index(tonic_note.upper()) + interval

    return NOTES[position % 12]


def _triad(tonic_note: str, scale_type: str) -> list[str]:
    """
    Generate the triad based on a given tonic note and scale mode.

    Args:
        tonic_note (str): The tonic note or the root note of the scale for
            which you want to determine the triad type.
        scale_type (str): The type of the scale. Currently supports only
            "major".

    Returns:
        list[str]: A list containing the notes of the triad.

    Raises:
        ValueError: If the tonic note is invalid.
        KeyError: If the scale mode does not exist or has not been implemented.

    Examples:
        >>> _triad("C", "major")
        ['C', 'E', 'G']

        >>> _triad("A", "minor")
        ['A', 'C', 'E']
    """
    degrees = (0, 2, 4)
    scale_notes, _ = scale(tonic_note, scale_type).values()

    return [scale_notes[degree] for degree in degrees]


def chord(tonic_note: str) -> dict[str, list[str]]:
    """
    Generate the notes and degrees for a chord based on a tonic note.

    Args:
        tonic_note (str): The tonic note representing the root note of the
            chord. It should specify the chord type:

            - No suffix for major
            - `m` for minor
            - `dim` for diminished
            - `+` for augmented
            - `m+` for minor augmented

    Returns:
        A dictionary containing the notes and their corresponding degrees.

    Examples:
        >>> chord("C")
        {'notes': ['C', 'E', 'G'], 'degrees': ['I', 'III', 'V']}

        >>> chord("Cm")
        {'notes': ['C', 'D#', 'G'], 'degrees': ['I', 'III-', 'V']}

        >>> chord("Cdim")
        {'notes': ['C', 'D#', 'F#'], 'degrees': ['I', 'III-', 'V-']}

        >>> chord("C+")
        {'notes': ['C', 'E', 'G#'], 'degrees': ['I', 'III', 'V+']}

        >>> chord("Cm+")
        {'notes': ['C', 'D#', 'G#'], 'degrees': ['I', 'III-', 'V+']}
    """

    if "dim" in tonic_note:
        key, _ = tonic_note.split("dim")
        tonic, third, fifth = _triad(key, "minor")
        keys = [tonic, third, _semitone(fifth, interval=-1)]
        degrees = ["I", "III-", "V-"]

    elif "m" in tonic_note:
        keys, degrees = _minor(tonic_note)

    elif "+" in tonic_note:
        key, _ = tonic_note.split("+")
        tonic, third, fifth = _triad(key, "major")
        keys = [tonic, third, _semitone(fifth, interval=+1)]
        degrees = ["I", "III", "V+"]

    else:
        keys = _triad(tonic_note, "major")
        degrees = ["I", "III", "V"]

    return {"notes": keys, "degrees": degrees}
