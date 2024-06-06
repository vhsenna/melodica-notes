from melodica_notes.chord import _triad
from melodica_notes.scale import scale


def _triad_scale(key: str, scale_key: list):
    """
    Determine whether the triad of a note is within the scale.

    Args:
        key (str): The tonic note or root note of the scale for which you want
            to determine the triad type.
        scale_key (list): A list of notes representing a specific musical
            scale.

    Returns:
        str: The tonic note of the triad based on the key and scale notes
            provided.

    Examples:
        >>> _triad_scale('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'C'
        >>> _triad_scale('D', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'Dm'
        >>> _triad_scale('B', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'Bdim'
    """
    tonic_note, third, fifth = _triad(key, 'major')

    match third in scale_key, fifth in scale_key:
        case True, True:
            return tonic_note
        case False, True:
            return f'{tonic_note}m'
        case False, False:
            return f'{tonic_note}dim'


def _convert_degrees(tonic_note: str, degree: str):
    """
    Converts a musical degree to its corresponding notation based on the given
        tonic note.

    Args:
        tonic_note (str): The tonic note of the chord (e.g., "C", "Cm", "Cdim").
        degree (str): The degree of the scale (e.g., "I", "II", "III").

    Returns:
        str: The converted degree.

    Examples:
        >>> _convert_degrees('C', 'I')
        'I'
        >>> _convert_degrees('Cm', 'I')
        'i'
        >>> _convert_degrees('Cdim', 'I')
        'i°'
    """
    if 'dim' in tonic_note:
        return f'{degree.lower()}°'

    if 'm' in tonic_note:
        return degree.lower()

    return degree


def harmonic(tonic_note: str, scale_mode: str) -> dict[str, list[str]]:
    """
    Generates a harmonic progression based on a note and a scale.

    Args:
        tonic_note (str): The root note of the harmonic progression.
        scale_mode (str): The scale, e.g., major, minor, etc.

    Returns:
        A harmonic progression containing chords and their corresponding degrees.

    Examples:
        >>> harmonic("C", "major")
        {'chords': ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bdim'], 'degrees': ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°']}

        >>> harmonic("C", "minor")
        {'chords': ['Cm', 'Ddim', 'D#', 'Fm', 'Gm', 'G#', 'A#'], 'degrees': ['i', 'ii°', 'III', 'iv', 'v', 'VI', 'VII']}
    """
    keys, _degrees = scale(tonic_note, scale_mode).values()
    chords = [_triad_scale(key, keys) for key in keys]
    degrees = [_convert_degrees(chord, degree)
               for chord, degree in zip(chords, _degrees)]

    return {'chords': chords, 'degrees': degrees}
