with open("puzzle-input1.txt") as puzzle_input:
    puzzle_data = puzzle_input.readlines()
    updated_data = [int(item.strip()) for item in puzzle_data]

# Day 1 Part 1 Problem

counter = 0
for n in range(1, len(updated_data)):
    previous_measurement = updated_data[n-1]
    if updated_data[n] > previous_measurement:
        counter += 1

print(f"This is the solution to Part 1: {counter}")

# Day 1 Part 2 Problem
list_of_sums = []
for n in range(0, len(updated_data)):
    try:
        total_sum = updated_data[n] + updated_data[n + 1] + updated_data[n + 2]
        list_of_sums.append(total_sum)
    except IndexError:
        continue

sum_counter = 0
for n in range(1, len(list_of_sums)):
    if list_of_sums[n] > list_of_sums[n-1]:
        sum_counter += 1

print(f"This is the solution to Part 2: {sum_counter}")



