# import packages
import re
from numpy import prod
import copy

# general functions
def file_content(which_input=["test input"==0, "real input"==1]):
    test = "AOC2023_test_3.txt"
    real = "AOC2023_real_3.txt"
    input_file = [test, real]
    f = open(input_file[which_input], "r") # open selected file
    f_content = f.read().splitlines() # read file, each line as an item in a list
    f.close()
    return f_content

# DAY THREE
# part 1
def day03_1(f_content):
    answer = 0
    for row in f_content:
        for number in re.finditer("\d+", row):
            mystring = ""
            engine_part = int(row[number.start():number.end()])
            x_start = number.start()
            x_end = number.end()
            if number.start() > 0:
                x_start -= 1
            if number.end() < len(row):
                x_end += 1
            if f_content.index(row) > 0:
                mystring += f_content[f_content.index(row)-1][x_start:x_end]
            mystring += f_content[f_content.index(row)][x_start:x_end]
            if f_content.index(row) < len(f_content)-1:
                mystring += f_content[f_content.index(row)+1][x_start:x_end]
            mystring = mystring.replace(".", "")
            if re.findall("\D", mystring) != []:
                answer += engine_part
    return answer

# part 2
def find_pattern(pattern, list_of_strings):
    item_positions = []
    for row in list_of_strings:
        y = list_of_strings.index(row)
        for item in re.finditer(pattern, row):
            item_positions.append([y, item.start(), item.end(), item.group()])
    return item_positions

def find_perimeter(list_of_middles, list_of_strings):
    perimeters = []
    for number in list_of_middles:
        y_max = len(list_of_strings)-1
        y_start = max(number[0], 1)-1
        y_end = min(number[0], y_max)+1
        x_start = max(number[1], 1)-1
        x_end = min(number[2], y_max)+1
        perimeters.append([y_start, y_end, x_start, x_end, number[3]])
    return perimeters

def find_gears_next_to_numbers(gears, numbers):
    new_gear_list = copy.deepcopy(gears)
    for num in numbers:
        for gear in new_gear_list:
            if gear[0] >= num[0] and gear[0] <= num[1] and gear[1] >= num[2] and gear[2] <= num[3]:
                gear.append(int(num[4]))
    for n in new_gear_list:
        del n[0:len(gears[0])]
    return new_gear_list

def day03_2(f_content):
    answer = 0
    gear_positions = find_pattern("\*", f_content)
    number_positions = find_pattern("\d+", f_content)
    number_perimeters = find_perimeter(number_positions, f_content)
    gears_next_to_numbers = find_gears_next_to_numbers(gear_positions, number_perimeters)
    for m in gears_next_to_numbers:
        if len(m) == 2:
            answer += prod(m)
    return(answer)

print("test, part 1:", day03_1(file_content(0)))
print("real, part 1:", day03_1(file_content(1)))
print("test, part 2:", day03_2(file_content(0)))
print("real, part 2:", day03_2(file_content(1)))
