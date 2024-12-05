from pathlib import Path
from collections import defaultdict
from functools import cmp_to_key

def part1(data_file: str | Path) -> int | str:
    is_ordering = True
    orderings = []
    updates = []
    with open(data_file, "rt") as infile:
        for line in infile.readlines():
            line = line.strip()
            if line == "":
                is_ordering = False
                continue

            if is_ordering:
                a, b = line.split('|')
                orderings.append((int(a), int(b)))
            else:
                updates.append([int(n) for n in line.split(',')])
    
    return part1_solution(orderings, updates)

def part2(data_file: str | Path) -> int | str:
    is_ordering = True
    orderings = []
    updates = []
    with open(data_file, "rt") as infile:
        for line in infile.readlines():
            line = line.strip()
            if line == "":
                is_ordering = False
                continue

            if is_ordering:
                a, b = line.split('|')
                orderings.append((int(a), int(b)))
            else:
                updates.append([int(n) for n in line.split(',')])
    
    return part2_solution(orderings, updates)

def part1_solution(orderings, updates):
    before_this = defaultdict(set)
    for a, b in orderings:
        before_this[a].add(b)

    good_updates = []
    for update in updates:
        good_update = True
        for i in range(len(update)):
            for j in range(i + 1, len(update)):
                if not update[j] in before_this[update[i]]:
                    good_update = False
                    break
            if not good_update:
                break
        
        if good_update:
            good_updates.append(update[len(update)//2])
    return sum(good_updates)

def part2_solution(orderings, updates):
    before_this = defaultdict(set)
    for a, b in orderings:
        before_this[a].add(b)

    bad_updates = []
    for update in updates:
        good_update = True
        for i in range(len(update)):
            for j in range(i + 1, len(update)):
                if not update[j] in before_this[update[i]]:
                    good_update = False
                    break
            if not good_update:
                break
        
        if not good_update:
            bad_updates.append(update)
    
    def compare(a, b):
        if a in before_this[b]:
            return 1
        else:
            return -1
    
    bad_updates = [sorted(upd, key=cmp_to_key(compare)) for upd in bad_updates]
    bad_updates = [upd[len(upd) // 2] for upd in bad_updates]

    return sum(bad_updates)

