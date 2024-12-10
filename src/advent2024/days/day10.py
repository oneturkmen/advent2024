from pathlib import Path
import collections
import string

def part1(data_file: str | Path) -> int | str:
    grid = []
    with open(data_file, "rt") as infile:
         for line in infile.readlines():
            grid.append(line.strip())

    return solution1(grid)

def part2(data_file: str | Path) -> int | str:
    grid = []
    with open(data_file, "rt") as infile:
         for line in infile.readlines():
            grid.append(line.strip())

    return solution2(grid)

def valid(i, j, n, m):
    return i >= 0 and j >= 0 and i < n and j < m


def solution1(grid):
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def dfs(i, j, grid, zeroes):
        # print((i, j))
        if grid[i][j] == '0':
            zeroes.add((i, j))
            return
        
        for di, dj in dirs:
            next_i = i + di
            next_j = j + dj

            if valid(next_i, next_j, n, m) and grid[next_i][next_j] != '.' and int(grid[next_i][next_j]) == int(grid[i][j]) - 1:
                dfs(next_i, next_j, grid, zeroes)
        
        return

    n = len(grid)
    m = len(grid[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '9':
                zeroes = set()
                dfs(i, j, grid, zeroes)
                # if len(zeroes) > 0:
                ans += len(zeroes)
                # print()
    return ans

def solution2(grid):
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def dfs(i, j, grid, zeroes):
        if grid[i][j] == '0':
            zeroes.append((i, j))
            return
        
        for di, dj in dirs:
            next_i = i + di
            next_j = j + dj

            if valid(next_i, next_j, n, m) and grid[next_i][next_j] != '.' and int(grid[next_i][next_j]) == int(grid[i][j]) - 1:
                dfs(next_i, next_j, grid, zeroes)
        
        return

    n = len(grid)
    m = len(grid[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '9':
                zeroes = list()
                dfs(i, j, grid, zeroes)
                # if len(zeroes) > 0:
                ans += len(zeroes)
                # print()
    return ans
