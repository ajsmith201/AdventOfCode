def parse_groups(puzzle_input):
    "Parse input into groups and then into individual numbers."
    return [[int(line) for line in block.splitlines()]
    for block in puzzle_input.split("\n\n")]

calories = parse_groups(puzzle.input_data)

cal_list = [sum(c) for c in calories]
print (max(cal_list))

cal_list.sort(reverse=True)
print (sum(cal_list[:3]))