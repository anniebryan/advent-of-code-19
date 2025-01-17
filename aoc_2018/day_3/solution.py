"""
Advent of Code 2018
Day 3: No Matter How You Slice It
"""

import click
import os
import pathlib
import regex as re


def get_claims(puzzle_input):
    pattern = r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'
    claims = [[int(y) for y in re.match(pattern, row).groups()] for row in puzzle_input]
    return claims


def generate_fabric():
    areas = dict.fromkeys(range(1000))  # keys are columns (left and right)
    for key in areas.keys():
        areas[key] = dict.fromkeys(range(1000))  # values are dicts that map row (up and down) to value
    return areas
    

def solve_part_1(puzzle_input: list[str]):
    claims = get_claims(puzzle_input)
    areas = generate_fabric()
    s = 0
    for c in claims:
        for h in range(c[1],c[1] + c[3]):
            for v in range(c[2],c[2] + c[4]):
                if areas[h][v] is None:
                    areas[h][v] = False  # one claim covers
                elif not areas[h][v]:
                    areas[h][v] = True  # at least one overlap
                    s += 1
    return s


def solve_part_2(puzzle_input: list[str]):
    claims = get_claims(puzzle_input)
    areas = generate_fabric()
    for c in claims:
        claim_id = c[0]
        for h in range(c[1], c[1] + c[3]):
            for v in range(c[2], c[2] + c[4]):
                if areas[h][v] is None:
                    areas[h][v] = [claim_id]  # one claim covers
                else:
                    areas[h][v].append(claim_id)  # at least one overlap
                    
    vals = []
    for i in range(1000):
        [vals.append(val) for val in areas[i].values() if val]
                
    claimed = dict.fromkeys(range(1, len(claims) + 1), False)
    for i, val in enumerate(vals):
        if len(val) > 1:
            for v in val:
                claimed[v] = True
    return list(claimed.keys())[list(claimed.values()).index(False)]


@click.command()
@click.option("-se", "--skip_example", is_flag=True, default=False)
@click.option("-sp", "--skip_puzzle", is_flag=True, default=False)
def main(skip_example: bool = False, skip_puzzle: bool = False) -> None:
    base_dir = pathlib.Path(__file__).parent
    example_files = sorted([fn for fn in os.listdir(base_dir) if fn.endswith(".txt") and "example" in fn])

    def _run_solution(filename: str, display_name: str):
        print(f"--- {display_name} ---")

        if not (filepath := (base_dir / filename)).exists():
            print(f"{filename} not found.")
            return

        with open(filepath) as file:
            puzzle_input = [line.strip("\n") for line in file]
            print(f"Part 1: {solve_part_1(puzzle_input)}")
            print(f"Part 2: {solve_part_2(puzzle_input)}")
        return

    if not skip_example:
        if len(example_files) < 2:
            _run_solution("example.txt", "Example")
        else:
            for i, filename in enumerate(example_files):
                _run_solution(filename, f"Example {i + 1}")

    if not skip_puzzle:
        _run_solution("puzzle.txt", "Puzzle")


if __name__ == "__main__":
    main()
