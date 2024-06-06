from pytest import mark
from typer.testing import CliRunner

from melodica_notes.cli import app

runner = CliRunner()


def test_scale_cli_should_exit_with_code_0():
    result = runner.invoke(app, ["scale"])
    assert result.exit_code == 0


@mark.parametrize('note', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
def test_scale_cli_should_contain_correct_scale(note,):
    result = runner.invoke(app, ["scale"])
    assert note in result.stdout


@mark.parametrize('note', ['F', 'G', 'A', 'A#', 'C', 'D', 'E'])
def test_scale_cli_should_contain_correct_scale_for_f(note):
    result = runner.invoke(app, ["scale", 'F'])
    assert note in result.stdout


@mark.parametrize('degree', ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'])
def test_scale_cli_should_contain_all_degrees(degree):
    result = runner.invoke(app, ["scale", 'F'])
    assert degree in result.stdout


@mark.parametrize('note', ['C', 'E', 'G'])
def test_chord_cli_should_contain_correct_response(note,):
    result = runner.invoke(app, ["chord"])
    assert note in result.stdout


@mark.parametrize('degree', ['I', 'III', 'V'])
def test_degree_cli_should_contain_correct_response(degree):
    result = runner.invoke(app, ["scale", 'F'])
    assert degree in result.stdout


@mark.parametrize('degree', ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°'])
def test_harmonic_cli_should_contain_all_degrees(degree):
    result = runner.invoke(app, ['harmonic', 'C'])
    assert degree in result.stdout


@mark.parametrize('chord', ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bdim'])
def test_harmonic_cli_should_contain_all_chords(chord):
    result = runner.invoke(app, ['harmonic', 'C'])
    assert chord in result.stdout
