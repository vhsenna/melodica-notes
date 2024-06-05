from pytest import mark
from typer.testing import CliRunner

from melodica_notes.cli import app

runner = CliRunner()


def test_scale_cli_should_exit_with_code_0():
    result = runner.invoke(app)
    assert result.exit_code == 0


@mark.parametrize('note', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
def test_scale_cli_should_contain_correct_scale(note):
    result = runner.invoke(app)
    assert note in result.stdout


@mark.parametrize('note', ['F', 'G', 'A', 'A#', 'C', 'D', 'E'])
def test_scale_cli_should_contain_correct_scale_for_f(note):
    result = runner.invoke(app, ['F'])
    assert note in result.stdout


@mark.parametrize('degree', ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'])
def test_scale_cli_should_contain_all_degrees(degree):
    result = runner.invoke(app, ['F'])
    assert degree in result.stdout
