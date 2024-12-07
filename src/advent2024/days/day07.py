from pathlib import Path
import itertools


def part1(data_file: str | Path) -> int | str:
    tests = []
    with open(data_file, "rt") as infile:
        for line in infile.readlines():
            target, nums = line.split(':')
            target = int(target)
            nums = [int(num) for num in nums.strip().split(' ')]

            tests.append((target, nums))

    return solution(tests)

def part2(data_file: str | Path) -> int | str:
    tests = []
    with open(data_file, "rt") as infile:
        for line in infile.readlines():
            target, nums = line.split(':')
            target = int(target)
            nums = [int(num) for num in nums.strip().split(' ')]

            tests.append((target, nums))

    return solution(tests, part2=True)
    

def valid(i, j, n, m):
    return i >= 0 and j >= 0 and i < n and j < m

def solution(tests, part2=False):
    operators = ['*', '+']
    if part2:
        operators.append('||')
    ans = 0
    for target, nums in tests:
        n_ops = len(nums) - 1
        possible = False
        for combination_ops in itertools.product(*[operators for _ in range(n_ops)]):
            total = nums[0]
            i = 1
            for op in combination_ops:
                if op == '*':
                    total = total * nums[i]
                elif op == '||':
                    total = int(str(total) + str(nums[i]))
                else:
                    total = total + nums[i]
                i += 1

            if total == target:
                possible = True
                break
                # ans += target
        if possible:
            ans += target
    
    return ans
    
def part2_solution(graph):
    return 0