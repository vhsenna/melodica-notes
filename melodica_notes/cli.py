from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from melodica_notes.chords import chord as _chord
from melodica_notes.scales import scale as _scale

console = Console()
app = Typer()


@app.command()
def scale(
        tonic_note: str = Argument("C", help="Tonic Note"),
        scale_mode: str = Argument("major", help="Scale Mode")
) -> None:
    """
    Display a scale based on a tonic note and scale mode.

    Args:
        tonic_note (str): The tonic note of the scale. Default is "C".
        scale_mode (str): The scale mode. Default is "major".

    Returns:
        None
    """
    table = Table()

    notes, degrees = _scale(tonic_note, scale_mode).values()

    for degree in degrees:
        table.add_column(degree)

    table.add_row(*notes)

    console.print(table)


@app.command()
def chord(tonic_note: str = Argument("C", help="Tonic Note")) -> None:
    """
    Display a chord based on a tonic note.

    Args:
        tonic_note (str): The tonic note of the chord. Default is "C".

    Returns:
        None
    """
    table = Table()

    notes, degrees = _chord(tonic_note).values()

    for degree in degrees:
        table.add_column(degree)

    table.add_row(*notes)

    console.print(table)
