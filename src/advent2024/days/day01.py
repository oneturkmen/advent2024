from pathlib import Path
from collections import defaultdict

def part1(data_file: str | Path) -> int | str:
    left_loc = []
    right_loc = []
    with open(data_file, "rt") as infile:
        for line in infile.readlines():
            l, r = line.strip().split()
            left_loc.append(int(l))
            right_loc.append(int(r))
    
    return part1_solution(left_loc, right_loc)


def part2(data_file: str | Path) -> int | str:
    left_loc = []
    right_loc = []
    with open(data_file, "rt") as infile:
        for line in infile.readlines():
            l, r = line.strip().split()
            left_loc.append(int(l))
            right_loc.append(int(r))
    
    return part2_solution(left_loc, right_loc)


def part1_solution(left_loc, right_loc):
    left_loc.sort()
    right_loc.sort()

    return sum([ abs(l - r) for l, r in zip(left_loc, right_loc)])


def part2_solution(left_loc, right_loc):
    right_count = defaultdict(lambda : 0)
    for num in right_loc:
        right_count[num] += 1

    return sum([ l * right_count[l] for l in left_loc])