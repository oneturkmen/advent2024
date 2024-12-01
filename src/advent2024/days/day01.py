from collections import Counter
from pathlib import Path


def read_data(data_file: str | Path) -> tuple[list[int], list[int]]:
    left_data = []
    right_data = []
    with open(data_file, "rt") as infile:
        for line in infile:
            l, r = line.strip().split()
            left_data.append(int(l))
            right_data.append(int(r))

    return left_data, right_data


def part1(data_file: str | Path) -> int | str:
    left_data, right_data = read_data(data_file)

    left_data.sort()
    right_data.sort()

    return sum(abs(l - r) for l, r in zip(left_data, right_data))


def part2(data_file: str | Path) -> int | str:
    left_data, right_data = read_data(data_file)

    counts = Counter(right_data)
    return sum(l * counts.get(l, 0) for l in left_data)
