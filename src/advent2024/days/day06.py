from pathlib import Path
import collections

def part1(data_file: str | Path) -> int | str:
    graph = []
    with open(data_file, "rt") as infile:
        for line in infile.readlines():
            graph.append(line.strip())
    return part1_solution(graph)

def part2(data_file: str | Path) -> int | str:
    graph = []
    with open(data_file, "rt") as infile:
        for line in infile.readlines():
            graph.append(line.strip())
    return part2_solution(graph)
    

def valid(i, j, n, m):
    return i >= 0 and j >= 0 and i < n and j < m

def part1_solution(graph, part2=False):
    n, m = len(graph), len(graph[0])
    dirs = ['^', '>', 'v', '<']
    direction_idx = None
    start_i, start_j = None, None

    for i in range(n):
        found = False
        for j in range(m):
            if graph[i][j] in dirs:
                start_i, start_j = i, j
                direction_idx = dirs.index(graph[i][j])
                found = True
                break
        if found:
            break
    
    queue = [(start_i, start_j, direction_idx)]

    move_direction_grid = {
        '>': (0, 1),
        '^': (-1, 0),
        '<': (0, -1),
        'v': (1, 0)
    }

    count_grid = collections.defaultdict(lambda : 0)
    visited_pos = set()
    while len(queue) > 0:
        i, j, dir_idx = queue.pop(0)
        visited_pos.add((i, j))
        
        move_direction = dirs[dir_idx]
        di, dj = move_direction_grid[move_direction]

        while valid(i + di, j + dj, n, m) and graph[i + di][j + dj] != '#':
            i += di
            j += dj
            visited_pos.add((i, j))
        
        if not valid(i + di, j + dj, n, m):
            break
        elif graph[i + di][j + dj] == '#':
            next_dir = (dir_idx + 1) % len(dirs)
            queue.append((i, j, next_dir))

        if part2:
            grid_place = f"{i},{j}"
            if count_grid[grid_place] >= 2:
                # We are stuck in a loop
                return -1
            else:
                count_grid[grid_place] += 1
    
    return len(visited_pos)

def replace_char(str, index, new_char):
    str_chars = list(str)
    str_chars[index] = new_char
    return ''.join(str_chars)
    
def part2_solution(graph):
    n, m = len(graph), len(graph[0])
    dirs = ['^', '>', 'v', '<']

    fruit_loops = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != '#' and graph[i][j] not in dirs:
                graph[i] = replace_char(graph[i], j, '#')
                if part1_solution(graph, part2=True) == -1:
                    fruit_loops += 1
                graph[i] = replace_char(graph[i], j, '.')

    
    return fruit_loops