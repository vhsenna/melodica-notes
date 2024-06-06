![logo](assets/logo.png){ width="150" .center }

# Melodica Notes

Melodica Notes is a command-line tool designed to provide information about musical scales, chords, and their corresponding notes.

## How to Use

Melodica Notes offers two main commands: `scale` and `chord`.

## Scale

To check a scale, simply use the `scale` command followed by the desired note and scale mode. For instance:

```bash
poetry run melodica-notes scale C
```

This will display the scale degrees and their corresponding notes:

```bash
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

### Changing the Scale Mode

You can specify scale mode by providing additional arguments. For example, to display the F# minor scale:

```bash
poetry run melodica-notes scales F# minor
```

Output:

```bash
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D  │ E   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

### Supported Scale Modes

At present, Melodica Notes supports major and minor scale modes.

## Chord

To check a chord, simply use the chord command followed by the desired chord name. For example:

```bash
poetry run melodica-notes chord A
```

Output:

```bash
┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ A │ C#  │ E │
└───┴─────┴───┘
```

### Chord variations

You can explore different chord variations by specifying the chord name. For instance:

```bash
poetry run melodica-notes chord D+
```

Output:

```bash
┏━━━┳━━━━━┳━━━━┓
┃ I ┃ III ┃ V+ ┃
┡━━━╇━━━━━╇━━━━┩
│ D │ F#  │ A# │
└───┴─────┴────┘
```

### Supported Chord Types

Currently, Melodica Notes supports major (default), minor (`m`), diminished (`dim`), and augmented (`+`) chords.

## Additional Information

For additional options and help, use the `--help` flag with any command:

```bash
poetry run melodica-notes scales --help
```

This will provide you with detailed information on available commands and options.

Enjoy exploring different musical scales and chords effortlessly with Melodica Notes!
