from pathlib import Path

from advent2024.days import dayxx


def test_dayxx(fixtures_path: Path):
    assert dayxx.part1(fixtures_path / "dayxx.txt") == 10


def test_dayxx(fixtures_path: Path):
    assert dayxx.part2(fixtures_path / "dayxx.txt") == 10
