# aoc_template.py

import pathlib
import sys


def parse(puzzle_input):
    return [line for line in puzzle_input.split()]


def find_calibration_values(line):
    num1 = num2 = None
    for char in line:
        try:
            if int(char) > 0:
                if not num1:
                    num1 = int(char)
                else:
                    num2 = int(char)
        except:
            continue
    if not num2:
        return (num1 * 10) + num1
    else:
        return (num1 * 10) + num2


def part1(data):
    sum = 0

    for line in data:
        sum += find_calibration_values(line)
    return sum


def replace_keys_with_values(input_string, replacement_dict):
    for key, value in replacement_dict.items():
        input_string = input_string.replace(key, f"{key[0]}{value}{key[-1]}")
    return input_string


def part2(data):
    dict_digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    sum = 0
    for line in data:
        converted_line = replace_keys_with_values(line, dict_digits)
        print(converted_line)
        sum += find_calibration_values(converted_line)
    return sum


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
