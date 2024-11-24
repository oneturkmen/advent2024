# Advent of Code 2024

Kevin's solutions to AoC 2024.

## Requirements

We use [`uv`](https://docs.astral.sh/uv/) as the manager of our python and packages. See their website for installation instructions.

## Setup

Just run

```bash
uv sync
```

## Running a Day

To run the code for a single day, use

```bash
uv run advent DAY [DATA_FILE]
```

If `DATA_FILE` is not specified, then the code will attempt to use a file called `data/day{DAY:02d}.txt`.

## Running a Test

To run tests, you can use

```bash
uv run py.test
```

## License

MIT
