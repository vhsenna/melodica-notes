![logo](assets/logo.png){ width="150" .center }

# Melodica Notes

Melodica Notes is a command-line tool designed to provide information about musical scales, chords, and harmonics.

## How to Use

The core of the application revolves around a command called `melodica-notes`.

Melodica Notes offers three subcommands: `scale`, `chord`, and `harmonic`.

## Scale

To check a scale, simply use the `scale` command followed by the desired note and scale mode.

At present, Melodica Notes supports `major` (default) and `minor` scale modes.

### Major Scale

```bash
poetry run melodica-notes scale C
```

```bash
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

### Minor Scale

```bash
poetry run melodica-notes scales F# minor
```

```bash
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D  │ E   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

## Chord

To check a chord, simply use the `chord` command followed by the desired chord name.

Melodica Notes supports the following chord types: major (default), `m` (minor), `dim` (diminished), `+` (augmented) and `m+` (minor augmented). For example:

### Major Chord

```bash
poetry run melodica-notes chord A
```

```bash
┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ A │ C#  │ E │
└───┴─────┴───┘
```

### Minor Chord

```bash
poetry run melodica-notes chord Em
```

```bash
┏━━━┳━━━━━━┳━━━┓
┃ I ┃ III- ┃ V ┃
┡━━━╇━━━━━━╇━━━┩
│ E │ G    │ B │
└───┴──────┴───┘
```

### Diminished Chord

```bash
poetry run melodica-notes chord Fdim
```

```bash
┏━━━┳━━━━━━┳━━━━┓
┃ I ┃ III- ┃ V- ┃
┡━━━╇━━━━━━╇━━━━┩
│ F │ G#   │ B  │
└───┴──────┴────┘
```

### Minor Augmented Chord

```bash
poetry run melodica-notes chord Gm+
```

```bash
┏━━━┳━━━━━━┳━━━━┓
┃ I ┃ III- ┃ V+ ┃
┡━━━╇━━━━━━╇━━━━┩
│ G │ A#   │ D# │
└───┴──────┴────┘
```

## Harmonic

You can access the harmonic using the `harmonic` command.

Melodica Notes supports `major` (default) and `minor` harmonic modes. For example:

### Harmonic Major

```bash
poetry run melodica-notes harmonic E
```

```bash
┏━━━┳━━━━━┳━━━━━┳━━━━┳━━━┳━━━━━┳━━━━━━━┓
┃ I ┃ ii  ┃ iii ┃ IV ┃ V ┃ vi  ┃ vii°  ┃
┡━━━╇━━━━━╇━━━━━╇━━━━╇━━━╇━━━━━╇━━━━━━━┩
│ E │ F#m │ G#m │ A  │ B │ C#m │ D#dim │
└───┴─────┴─────┴────┴───┴─────┴───────┘
```

### Harmonic Minor

```bash
poetry run melodica-notes harmonic F# minor
```

```bash
┏━━━━━┳━━━━━━━┳━━━━━┳━━━━┳━━━━━┳━━━━┳━━━━━┓
┃ i   ┃ ii°   ┃ III ┃ iv ┃ v   ┃ VI ┃ VII ┃
┡━━━━━╇━━━━━━━╇━━━━━╇━━━━╇━━━━━╇━━━━╇━━━━━┩
│ F#m │ G#dim │ A   │ Bm │ C#m │ D  │ E   │
└─────┴───────┴─────┴────┴─────┴────┴─────┘
```

## Additional Information

For additional options and help, use the `--help` flag with any command:

```bash
poetry run melodica-notes [COMMANDS] --help

╭─ Commands ─────────────────────────────────────────────────────╮
│ chord                                                          │
│ harmonic                                                       │
│ scale                                                          │
╰────────────────────────────────────────────────────────────────╯
```

This will provide you with detailed information on available commands and options.

Enjoy exploring different musical scales and chords effortlessly with Melodica Notes!
