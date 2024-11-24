import importlib
from pathlib import Path

import typer

app = typer.Typer()


@app.command()
def run(day: int, data_file: str | None = None) -> None:
    """Run an AOC day"""
    mod = importlib.import_module(f"advent2024.days.day{day:02d}")

    if not data_file:
        data_file = Path.cwd() / "data" / f"day{day:02d}.txt"

    print(f"Part 1: {mod.part1(data_file)}")
    print(f"Part 2: {mod.part2(data_file)}")


if __name__ == "__main__":
    app()
