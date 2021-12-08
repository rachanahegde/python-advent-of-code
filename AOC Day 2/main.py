with open("day_2_puzzle_input.txt") as puzzle_input:
    puzzle_data = puzzle_input.readlines()
    updated_data = [item.strip() for item in puzzle_data]

# Day 2 Puzzle Part 1
horizontal_position = 0
depth = 0

for item in updated_data:
    if 'forward' in item:
        horizontal_position += int(item.split()[1])
    elif 'down' in item:
        depth += int(item.split()[1])
    else:
        depth -= int(item.split()[1])

final_calculation = horizontal_position * depth
print(f"This is the solution to part 1 of the puzzle: {final_calculation}")

# Day 2 Puzzle Part 2
horizontal_position = 0
depth = 0
aim = 0

for item in updated_data:
    if 'down' in item:
        aim += int(item.split()[1])
    elif 'up' in item:
        aim -= int(item.split()[1])
    else:
        horizontal_position += int(item.split()[1])
        depth += (aim * int(item.split()[1]))

new_calculation = horizontal_position * depth
print(f"This is the solution to Part 2: {new_calculation}")
