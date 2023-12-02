# aoc_template.py

import pathlib
import sys
import numpy as np

CUBES = set(['blue', 'green', 'red'])
CUBES_THRESHOLD = [14, 13, 12]

def parse(puzzle_input):

    games = {}

    for line in puzzle_input.split('\n'):

      id_idx = line.index('Game') + len('Game') + 1
      last_id_idx = line.index(':')
      id = int(line[id_idx:last_id_idx])

      sets = line[last_id_idx+2:].split('; ')

      game = [[0 for _ in range(len(CUBES))] for _ in range(len(sets))]

      for idx, each_set in enumerate(sets):
          tmp = each_set.split(', ')
          for colour_str in tmp:

            for colour_idx, colour in enumerate(CUBES):
                try:
                  colour_pos = colour_str.index(colour)
                except:
                    continue

                game[idx][colour_idx] = int(colour_str[:colour_pos - 1])

      games[id] = game
    return games

def part1(data):
    """Solve part 1."""
    sum = 0
    for key, game in data.items():
        eligible = True
        for play in game:
            for idx, threshold in enumerate(CUBES_THRESHOLD):
                if play[idx] > threshold:
                    eligible = False
                    break
        if eligible:
            sum += key


    return sum

def part2(data):
    """Solve part 2."""
    sum = 0
    for key, game in data.items():
        eligible = True
        required = [0, 0, 0]
        for play in game:
            for idx, threshold in enumerate(CUBES_THRESHOLD):
                required[idx] = max(required[idx], play[idx])
        if eligible:
            sum += np.prod(required)

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
