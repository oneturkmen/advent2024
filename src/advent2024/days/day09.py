from pathlib import Path
import collections
import string

def part1(data_file: str | Path) -> int | str:
    disk = ""
    with open(data_file, "rt") as infile:
         disk = infile.readline()
            # grid.append(line.strip())

    return solution1(disk)

def part2(data_file: str | Path) -> int | str:
    disk = ""
    with open(data_file, "rt") as infile:
         disk = infile.readline()
            # grid.append(line.strip())

    return solution2(disk)

def solution1(disk):
    n = len(disk)
    disk_layout = []

    # Represent
    is_busy = True
    for i in range(n):
        if is_busy:
            disk_layout.extend([i//2] * int(disk[i]))
        else:
            disk_layout.extend(['.'] * int(disk[i]))
        
        is_busy = not is_busy
    
    # Defragment
    i = 0
    j = len(disk_layout) - 1
    while i < j:
        if disk_layout[i] == '.':
            while disk_layout[j] == '.':
                j -= 1
            
            disk_layout[i] = disk_layout[j]
            j -= 1
        i += 1

    # Calculate
    checksum = 0
    for k in range(i+1):
        if disk_layout[k] != '.':
            checksum += disk_layout[k] * k

    return checksum


def solution2(disk):
    n = len(disk)
    disk_layout = []

    # Represent
    files = dict()
    is_busy = True
    for i in range(n):
        if is_busy:
            disk_layout.extend([i//2] * int(disk[i]))
            files[i//2] = int(disk[i])
        else:
            disk_layout.extend(['.'] * int(disk[i]))
        
        is_busy = not is_busy

    files = dict(sorted(files.items(), key=lambda item: -item[0]))

    # Find free spaces
    free_spaces = []
    i = 0
    while i < len(disk_layout):
        if disk_layout[i] != '.':
            i += 1
            continue
        j = i
        while j < len(disk_layout) and disk_layout[j] == '.':
            j += 1
        
        free_spaces.append((i, j-1))
        i = j
    
    # Start filling with largest digits
    digit_idx = [disk_layout.index(d) for d in range(0, 10000)]

    for digit, sz in files.items():
        # print("".join([str(ooo) for ooo in disk_layout]))
        k = 0
        while k < len(free_spaces):
            i, j = free_spaces[k]

            if digit_idx[digit] <= j:
                break

            if i > j:
                k += 1
                continue

            window_length = j - i + 1

            if sz <= window_length:
                current_idx = disk_layout.index(digit)
                disk_layout[current_idx:current_idx + sz] = ['.'] * sz
                disk_layout[i:i+sz] = [digit] * sz
                free_spaces[k] = (i+sz, j)
                break
            k += 1

    # Calculate
    checksum = 0
    for k in range(len(disk_layout)):
        if disk_layout[k] != '.':
            checksum += disk_layout[k] * k

    return checksum