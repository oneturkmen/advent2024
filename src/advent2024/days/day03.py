from pathlib import Path
from collections import defaultdict

def part1(data_file: str | Path) -> int | str:
    strings = []
    with open(data_file, "rt") as infile:
        for line in infile.readlines():
            line = line.strip()
            strings.append(line)
    
    return part1_solution(strings)


def part2(data_file: str | Path) -> int | str:
    strings = []
    with open(data_file, "rt") as infile:
        for line in infile.readlines():
            line = line.strip()
            strings.append(line)
    
    return part2_solution(strings)


def part1_solution(strings):
    import re
    ans = 0

    for string in strings:
       matches = re.findall(r"mul\(\d+,\d+\)", string)
       for match in matches:
           match = match[4:]
           match = match[:-1]
        #    print(match)
           d1, d2 = match.split(',')
           ans += int(d1) * int(d2)
    return ans


def part2_solution(strings):
    import re
    ans = 0

    enabled = True
    for string in strings:
        matches = re.findall(r"(mul\(\d+,\d+\)|don't\(\)|do\(\))", string)
        for match in matches:
            # print(matches)
            if match == "don't()":
                enabled = False
            elif match == "do()":
                enabled = True

            if enabled and match.startswith("mul"):
                match = match[4:]
                match = match[:-1]
                # print(match)
                d1, d2 = match.split(',')
                ans += int(d1) * int(d2)
    return ans