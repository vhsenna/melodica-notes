from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from melodica_notes.scales import scale

console = Console()
app = Typer()


@app.command()
def scales(
        tonic_note: str = Argument("C", help="Tonic Note"),
        scale_mode: str = Argument("major", help="Scale Mode")
):
    table = Table()

    notes, degrees = scale(tonic_note, scale_mode).values()

    for degree in degrees:
        table.add_column(degree)

    table.add_row(*notes)

    console.print(table)
