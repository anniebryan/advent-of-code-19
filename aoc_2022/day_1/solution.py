"""
Advent of Code 2022
Day 1: Calorie Counting
"""

def get_max_three(a, b, c, current_elf):
    if current_elf > c:
        c = current_elf
        if current_elf > b:
            b, c = current_elf, b
            if current_elf > a:
                a, b = current_elf, a
    return a, b, c


def max_three_elves(puzzle_input):
    a, b, c = 0, 0, 0
    current_elf = 0
    for cal in puzzle_input:
        if cal == '':
            a, b, c = get_max_three(a, b, c, current_elf)
            current_elf = 0
        else:
            current_elf += int(cal)
    return get_max_three(a, b, c, current_elf)


def solve_part_1(puzzle_input: list[str]):
    return max_three_elves(puzzle_input)[0]


def solve_part_2(puzzle_input: list[str]):
    return sum(max_three_elves(puzzle_input))