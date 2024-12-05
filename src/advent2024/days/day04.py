from pathlib import Path
from collections import defaultdict

def part1(data_file: str | Path) -> int | str:
    graph = []
    with open(data_file, "rt") as infile:
        for line in infile.readlines():
            line = line.strip()
            graph.append(line)
    
    return part1_solution(graph)


def part2(data_file: str | Path) -> int | str:
    graph = []
    with open(data_file, "rt") as infile:
        for line in infile.readlines():
            line = line.strip()
            graph.append(line)
    
    return part2_solution(graph)

def valid(i, j, n, m):
    return i >= 0 and j >= 0 and i < n and j < m


def part1_solution(graph):
    n = len(graph)
    m = len(graph[0])
    dirs = [(-1, 0), (-1, -1), (1, 1), (0, -1), (1, 0), (0, 1), (-1, 1), (1, -1)]

    counts = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'X':
                for di, dj in dirs:
                    c = 0
                    word = graph[i][j]
                    new_i = i
                    new_j = j
                    while c < 3:
                        new_i += di
                        new_j += dj
                        if valid(new_i, new_j, n, m):
                            word += graph[new_i][new_j]
                        c += 1
                    if word == "XMAS":
                        counts += 1
    return counts


def part2_solution(graph):
    n = len(graph)
    m = len(graph[0])
    counts = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'A':
                # Left top
                top_left = (i - 1, j - 1)
                top_right = (i - 1, j + 1)
                bottom_right = (i + 1, j + 1)
                bottom_left = (i + 1, j - 1)

                if valid(top_left[0], top_left[1], n, m) and valid(top_right[0], top_right[1], n, m) \
                    and valid(bottom_left[0], bottom_left[1], n, m) and valid(bottom_right[0], bottom_right[1], n, m):

                    xmas = 0

                    top_left = graph[i - 1][j - 1]
                    top_right = graph[i - 1][j + 1]
                    bottom_right = graph[i + 1][j + 1]
                    bottom_left = graph[i + 1][j - 1]

                    if (top_left == 'S' and bottom_right == 'M') or (top_left == 'M' and bottom_right == 'S'):
                        xmas += 1
                    if (top_right == 'S' and bottom_left == 'M') or (top_right == 'M' and bottom_left == 'S'):
                        xmas += 1

                    if xmas == 2:
                        counts += 1
    return counts
