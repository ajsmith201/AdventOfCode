def parse_pairs(puzzle_input):
    """Parse input."""
    return [pair for pair in puzzle_input.splitlines()]

pairs = parse_pairs(puzzle.input_data)

score_dict = {
    'A X' : 4,
    'A Y' : 8,
    'A Z' : 3,
    'B X' : 1,
    'B Y' : 5,
    'B Z' : 9,
    'C X' : 7,
    'C Y' : 2,
    'C Z' : 6
}

score = 0
for pair in pairs:
    score += score_dict[pair]
print(score)

second_dict = {
    'A X' : 3,
    'A Y' : 4,
    'A Z' : 8,
    'B X' : 1,
    'B Y' : 5,
    'B Z' : 9,
    'C X' : 2,
    'C Y' : 6,
    'C Z' : 7
}
second_score = 0
for pair in pairs:
    second_score += second_dict[pair]
print(second_score)