# import packages
import os
import numpy as np

# general functions
def file_content(which_input=["test input"==0, "real input"==1]):
    test = "AOC2023_test_4.txt"
    real = "AOC2023_real_4.txt"
    input_file = [test, real]
    f = open(input_file[which_input], "r") # open selected file
    f_content = f.read().splitlines() # read file, each line as an item in a list
    f.close()
    return f_content

# DAY FOUR
# part 1
def day04_1(f_content):
    answer = 0
    for row in f_content:
        lists = row.replace("|", ": ").split(":")
        card = "".join(filter(str.isdigit, lists[0]))
        winning_numbers = [int(x) for x in lists[1].split()]
        my_numbers = [int(x) for x in lists[2].split()]
        hits = len(np.intersect1d(winning_numbers, my_numbers))
        answer += int(2**(hits-1))
    return answer

# part 2
def day04_2(f_content):
    answer = 0
    number_of_cards = [0]*len(f_content)
    for row in f_content:
        lists = row.replace("|", ": ").split(":")
        card = "".join(filter(str.isdigit, lists[0]))
        winning_numbers = [int(x) for x in lists[1].split()]
        my_numbers = [int(x) for x in lists[2].split()]
        number_of_cards[int(card)-1] += 1
        hits = len(np.intersect1d(winning_numbers, my_numbers))
        for n in range(0, hits):
            number_of_cards[int(card)+n] += 1*number_of_cards[int(card)-1]
        answer = sum(number_of_cards)
    return answer

print("test, part 1:", day04_1(file_content(0)))
print("real, part 1:", day04_1(file_content(1)))
print("test, part 2:", day04_2(file_content(0)))
print("real, part 2:", day04_2(file_content(1)))