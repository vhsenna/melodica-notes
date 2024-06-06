from melodica_notes.scales import NOTES, scale


def _minor(tonic_note):
    key, _ = tonic_note.split("m")

    if "+" in tonic_note:
        tonic, third, fifth = triad(key, "minor")
        keys = [tonic, third, semitone(fifth, interval=1)]
        degrees = ["I", "III-", "V+"]
    else:
        keys = triad(key, "minor")
        degrees = ["I", "III-", "V"]

    return keys, degrees


def semitone(tonic_note, *, interval):
    position = NOTES.index(tonic_note.upper()) + interval

    return NOTES[position % 12]


def triad(tonic_note, scale_mode):
    degrees = (0, 2, 4)
    scale_notes, _ = scale(tonic_note, scale_mode).values()

    return [scale_notes[degree] for degree in degrees]


def chord(tonic_note: str) -> dict[str, list[str]]:
    """
    Generate the notes and degrees for a chord based on a tonic note.

    Parameters:
        tonic_note (str): The musical note serving as the tonic of the chord. It should specify the chord type:

            - No suffix for major
            - "m" for minor
            - "dim" for diminished
            - "+" for augmented
            - "m+" for minor augmented

    Returns:
        dict: A dictionary containing:

            - "notes": A list of the notes in the chord.
            - "degrees": A list of the corresponding degrees of the chord.

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
        tonic, third, fifth = triad(key, "minor")
        keys = [tonic, third, semitone(fifth, interval=-1)]
        degrees = ["I", "III-", "V-"]

    elif "m" in tonic_note:
        keys, degrees = _minor(tonic_note)

    elif "+" in tonic_note:
        key, _ = tonic_note.split("+")
        tonic, third, fifth = triad(key, "major")
        keys = [tonic, third, semitone(fifth, interval=+1)]
        degrees = ["I", "III", "V+"]

    else:
        keys = triad(tonic_note, "major")
        degrees = ["I", "III", "V"]

    return {"notes": keys, "degrees": degrees}
