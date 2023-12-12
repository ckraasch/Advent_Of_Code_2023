# import packages
import os
import numpy as np

# general functions
def file_content(which_input=["test input"==0, "real input"==1]):
    test = "AOC2023_test_5.txt"
    real = "AOC2023_real_5.txt"
    input_file = [test, real]
    f = open(input_file[which_input], "r") # open selected file
    f_content = f.read().splitlines() # read file, each line as an item in a list
    f.close()
    return f_content

# DAY FIVE
# part 1
def remove_first_entry(old_string):
    new_string = old_string[1:]
    return new_string

def make_sublists(giant_list):
    sublist, old_list = [], []
    for n in giant_list:
        if n == [] or giant_list.index(n) == len(giant_list)-1:
            old_list.append(sublist)
            sublist = []
        else:
            sublist.append(n)
    return old_list

def remove_everything_but_numbers(new_list):
    new_list[0][0].pop(0)
    new_list[0].insert(0, [])
    for m in new_list:
        new_list[new_list.index(m)] = turn_str_into_int(m[1:])
    return new_list

def turn_str_into_int(list_of_strings):
    for i in list_of_strings:
        list_of_strings[list_of_strings.index(i)] = list(map(int, i))
    return list_of_strings

def go_through_map(prev_val, new_list, n):
    next_val = prev_val
    for item in new_list[n]:
        diff = 0
        next_val_range_start, prev_val_range_start, range_length = item
        if next_val == prev_val and prev_val_range_start <= prev_val <= (prev_val_range_start+range_length):
            diff = next_val_range_start - prev_val_range_start
            next_val = prev_val + diff
    return next_val

def find_locations(seed, new_list):
    next_val = seed
    for n in range(1, len(new_list)):
        next_val = go_through_map(next_val, new_list, n)
    return next_val

def day05_1(f_content):
    answer = None
    giant_list = []
    [giant_list.append(row.split()) for row in f_content]
    old_list = make_sublists(giant_list)
    new_list = remove_everything_but_numbers(old_list)
    seed_list = new_list[0][0]
    for seed in seed_list:
        if answer == None:
            answer = find_locations(seed, new_list)
        else:
            answer = min(answer, find_locations(seed, new_list))
    return answer

# part 2
def day05_2(f_content):
    answer = None
    giant_list = []
    [giant_list.append(row.split()) for row in f_content]
    old_list = make_sublists(giant_list)
    new_list = remove_everything_but_numbers(old_list)
    seed_list = new_list[0][0]
    for first_seed, seeds_len in zip(seed_list[::2], seed_list[1::2]):
        last_seed = first_seed+seeds_len
        for i in range(first_seed, last_seed):
            if answer == None:
                answer = find_locations(i, new_list)
            else:
                answer = min(answer, find_locations(i, new_list))
    return answer

print("test, part 1:", day05_1(file_content(0)))
print("real, part 1:", day05_1(file_content(1)))
print("test, part 2:", day05_2(file_content(0)))
# print("real, part 2:", day05_2(file_content(1))) # takes too long, not sure if it works
