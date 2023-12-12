# import packages
import os
import re

# general functions
def file_content(which_input=["test input"==0, "real input"==1], which_part=["part 1"==0, "part 2"==1]):
    test = ["AOC2023_test_1.1.txt", "AOC2023_test_1.2.txt"]
    real = "AOC2023_real_1.txt"
    input_file = [test[which_part], real]
    f = open(input_file[which_input], "r") # open selected file
    f_content = f.read().splitlines() # read file, each line as an item in a list
    f.close()
    return f_content

# DAY ONE
# part 1
def day01_1(f_content):
    answer = 0
    for row in f_content:
        x = ''.join(filter(str.isdigit, row))
        answer += int(x[:1] + x[-1:])
    return answer

# part 2
def swap_numbers_with_words(mystring):
    swap_pattern = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    lst = list(mystring)
    for word in swap_pattern:
        for match in re.finditer(word, mystring):
            lst[match.start()] = (str(swap_pattern.index(word) + 1))
    return lst

def day01_2(f_content):
    answer = 0
    for row in f_content:
        new_row = swap_numbers_with_words(row)
        x = ''.join(filter(str.isdigit, new_row))
        answer += int(x[:1] + x[-1:])
    return answer

print("test, part 1:", day01_1(file_content(0, 0)))
print("real, part 1:", day01_1(file_content(1, 0)))
print("test, part 2:", day01_2(file_content(0, 1)))
print("real, part 2:", day01_2(file_content(1, 1)))