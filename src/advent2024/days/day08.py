from pathlib import Path
import collections
import string

def part1(data_file: str | Path) -> int | str:
    grid = []
    with open(data_file, "rt") as infile:
        for line in infile.readlines():
            grid.append(line.strip())

    return solution(grid)

def part2(data_file: str | Path) -> int | str:
    grid = []
    with open(data_file, "rt") as infile:
        for line in infile.readlines():
            grid.append(line.strip())

    return solution(grid, part2=True)

def valid(i, j, n, m):
    return i >= 0 and j >= 0 and i < n and j < m

def solution(grid, part2=False):
    antenna_names = set(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    
    n, m = len(grid), len(grid[0])

    # Get similar nodes
    antenna_positions = collections.defaultdict(list)
    for i in range(n):
        for j in range(m):
            curr = grid[i][j]
            if curr in antenna_names:
                antenna_positions[curr].append((i, j))
    
    # Find closest for each
    placements = set()
    part2_placements = set()
    for positions in antenna_positions.values():
        k = len(positions)

        for i in range(k):
            a = positions[i]

            part2_placements.add(a)
            for j in range(k):
                b = positions[j]
                part2_placements.add(b)

                diff_i = a[0] - b[0]
                diff_j = a[1] - b[1]

                if not (a[0] + diff_i == b[0] and a[1] + diff_j == b[1]):
                    if valid(a[0] + diff_i, a[1] + diff_j, n, m):
                        placements.add((a[0] + diff_i, a[1] + diff_j))

                # Part 2
                if part2:
                    if not (a[0] + diff_i == b[0] and a[1] + diff_j == b[1]):
                        tmp_i = a[0]
                        tmp_j = a[1]
                        while valid(tmp_i + diff_i, tmp_j + diff_j, n, m):
                            tmp_i += diff_i
                            tmp_j += diff_j
                            part2_placements.add((tmp_i, tmp_j))
                # End of part 2

    return len(part2_placements) if part2 else len(placements)
