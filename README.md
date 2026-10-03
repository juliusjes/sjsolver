# sjsolver

Simple DFS solver for the [Sanajahti](https://sanajahti.fi/) word game.

## Requirements

- Python 3.8+
- pandas

## Installation

Clone the repository and install the package:

```bash
pip install .
```
or for editing using the "-e" flag.

## Usage

Run the solver with:

```bash
python -m sjsolver.main --chars uuuiiikkk --height 3 --width 3
```

The `--chars` argument defines the letters on the game board. The `--height` and `--width` arguments define the board dimensions.

For example:

```text
u u u
i i i
k k k
```

with:

```bash
python -m sjsolver.main --chars uuuiiikkk --height 3 --width 3
```

## Project structure

```text
sjsolver/
├── pyproject.toml
├── src/
│   └── sjsolver/
└── README.md
```

## Development

The project uses [setuptools](https://setuptools.pypa.io/) as its build backend.

Package discovery is configured to use the `src` directory:

```toml
[tool.setuptools.packages.find]
where = ["src"]
```

## License

License information has not yet been specified.