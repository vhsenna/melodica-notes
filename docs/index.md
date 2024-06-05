![logo](assets/logo.png){ width="150" .center }

# Melodica Notes

Melodica Notes is a command-line tool for displaying musical scales and their corresponding notes.

## How to Use

To use Melodica Notes, simply call the scales via the command line. For example:

```bash
poetry run scales
```

This will return the corresponding scale degrees and their notes:

```bash
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

### Changing the Tonic Note

You can also change the tonic note of the scale. This is specified as the first parameter in the command line. For example, to display the F# scale, use:

```bash
poetry run scales F#
```

Output:

```bash
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D# │ F   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

## Changing the Scale Mode

You can also change the mode of the scale. This is specified as the second parameter in the command line. For example, to display the D# major scale:

```bash
poetry run scales D# major
```

Output:

```bash
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ D# │ F  │ G   │ G# │ A# │ C  │ D   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

## Further Details on the CLI

To explore additional options, simply utilize the `--help` flag.

```bash
poetry run scales --help
```

Output:

```bash

 Usage: scales [OPTIONS] [TONIC_NOTE] [SCALE_MODE]

╭─ Arguments ───────────────────────────────────────────────────────────────╮
│   tonic_note      [TONIC_NOTE]  Tonic Note [default: C]                   │
│   scale_mode      [SCALE_MODE]  Scale Mode [default: major]               │
╰───────────────────────────────────────────────────────────────────────────╯
```

Enjoy using Melodica Notes to explore different musical scales effortlessly!
