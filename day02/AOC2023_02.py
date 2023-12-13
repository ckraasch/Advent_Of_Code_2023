# import packages
import re
from numpy import prod

# general functions
def file_content(which_input=["test input"==0, "real input"==1]):
    test = "AOC2023_test_2.txt"
    real = "AOC2023_real_2.txt"
    input_file = [test, real]
    f = open(input_file[which_input], "r") # open selected file
    f_content = f.read().splitlines() # read file, each line as an item in a list
    f.close()
    return f_content

# DAY TWO
# part 1
def are_socks_in_range(numbers_of_socks, sock_colour):
    max_amount, colour = [12, 13, 14], ["red", "green", "blue"]
    n = 0 if numbers_of_socks > max_amount[colour.index(sock_colour)] else 1
    return n

def day02_1(f_content):
    answer, numbers_of_socks, evenodd = 0, 0, 1
    for row in f_content:
        game = int(row[5:row.find(": ")])
        for i in re.split("; ", row[row.find(": ")+2:]):
            for subset in re.split(", |\s", i):
                if evenodd % 2 == 0:
                    game *= are_socks_in_range(numbers_of_socks, subset)
                else:
                    numbers_of_socks = int(subset)
                evenodd += 1
        answer += game
    return answer

# part 2
def day02_2(f_content):
    answer, counter, evenodd = 0, 0, 1
    colour = ["red", "green", "blue"]
    for row in f_content:
        min_amount = [0, 0, 0]
        for i in re.split("; ", row[row.find(": ")+2:]):
            for n in re.split(", |\s", i):
                    if evenodd % 2 == 0:
                        if counter > min_amount[colour.index(n)]:
                            min_amount[colour.index(n)] = counter
                    else:
                        counter = int(n)
                    evenodd += 1
        answer += prod(min_amount)
    return answer

print("test, part 1:", day02_1(file_content(0)))
print("real, part 1:", day02_1(file_content(1)))
print("test, part 2:", day02_2(file_content(0)))
print("real, part 2:", day02_2(file_content(1)))
