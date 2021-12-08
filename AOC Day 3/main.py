# with open("day_3_puzzle_input.txt") as puzzle_input:
#     puzzle_data = puzzle_input.readlines()
#     updated_data = [item.strip() for item in puzzle_data]

updated_data = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010',
                '01010']

# Day 3 Puzzle Part 1
gamma_rate = []
epsilon_rate = []

first_bit_list = []
second_bit_list = []
third_bit_list = []
fourth_bit_list = []
fifth_bit_list = []
sixth_bit_list = []
seventh_bit_list = []
eighth_bit_list = []
ninth_bit_list = []
tenth_bit_list = []
twelfth_bit_list = []

for number in updated_data:
    digits_list = [int(i) for i in number]
    print(len(digits_list))
    for n in range(0, len(digits_list)):
        first_bit_list.append(digits_list[0])
        second_bit_list.append(digits_list[1])
        third_bit_list.append(digits_list[2])
        fourth_bit_list.append(digits_list[3])
        fifth_bit_list.append(digits_list[4])

print(first_bit_list)
print(len(first_bit_list))
print(second_bit_list)
# print(gamma_rate)



