from pathlib import Path
from collections import defaultdict

def part1(data_file: str | Path) -> int | str:
    reports = []
    with open(data_file, "rt") as infile:
        for line in infile.readlines():
            levels = [int(num) for num in line.strip().split()]
            reports.append(levels)
    
    return part1_solution(reports)


def part2(data_file: str | Path) -> int | str:
    reports = []
    with open(data_file, "rt") as infile:
        for line in infile.readlines():
            levels = [int(num) for num in line.strip().split()]
            reports.append(levels)
    
    return part2_solution(reports)


def part1_solution(reports):
    ans = 0
    for levels in reports:
        report_status = True
        increasing = levels[0] > levels[1]
        for i in range(len(levels) - 1):
            if increasing and levels[i] <= levels[i + 1]:
                report_status = False
                break
            if not increasing and levels[i] > levels[i + 1]:
                report_status = False
                break
            if not 1 <= abs(levels[i] - levels[i + 1]) <= 3:
                report_status = False
                break
        
        if report_status:
            ans += 1
    
    return ans

def part2_solution(reports):
    original = 0
    unsafe_reports = []
    for levels in reports:
        report_status = True
        increasing = levels[0] > levels[1]
        for i in range(len(levels) - 1):
            if increasing and levels[i] <= levels[i + 1]:
                report_status = False
                break
            if not increasing and levels[i] > levels[i + 1]:
                report_status = False
                break
            if not 1 <= abs(levels[i] - levels[i + 1]) <= 3:
                report_status = False
                break
        
        if report_status:
            original += 1
        else:
            unsafe_reports.append(levels)
    
    fixed = 0
    for levels in unsafe_reports:
        for mask_i in range(len(levels)):
            new_levels = [l for i, l in enumerate(levels) if i != mask_i ]
            report_status = True
            increasing = new_levels[0] > new_levels[1]

            for i in range(len(new_levels) - 1):
                if increasing and new_levels[i] <= new_levels[i + 1]:
                    report_status = False
                    break
                if not increasing and new_levels[i] > new_levels[i + 1]:
                    report_status = False
                    break
                if not 1 <= abs(new_levels[i] - new_levels[i + 1]) <= 3:
                    report_status = False
                    break
            
            if report_status == True:
                fixed += 1
                break

    return original + fixed