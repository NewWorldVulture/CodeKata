#!/usr/bin/python3
# Kata02: Karate Chop
# By Ada

# Goal: Implement a binary search routine. Testing with this script
# http://codekata.com/kata/kata02-karate-chop/

import Kata02_03 as chopper
import os


# iterates through all unit tests
def assert_equal(test_case, counter):
    # print()
    try:
        if test_case[0] == chopper.chop(test_case[1], test_case[2]):
            print(f"{str(counter).zfill(2)} : Pass")
        else:
            print(f"{str(counter).zfill(2)} : ->Fail")
    # If we run into an error, print out the error
    except Exception as e:
        print(str(counter).zfill(2),": ","->Fail with Error:")
        print(e)New File

# Iterates through all test cases using
def the_ringer():
    for counter, test_case in enumerate(ringer_list):
        assert_equal(test_case, counter)

# === UNIT TESTS ===
# First element is the correct index of the value being searched for
# Second element is the target integer being searched for
# The third element is the list being searched for
ringer_list = [
    [-1, 3, []],            # 00
    [-1, 3, [1]],           # 01

    [0, 1, [1]],           # 02
    [0, 1, [1, 3, 5]],     # 03
    [1, 3, [1, 3, 5]],     # 04
    [2, 5, [1, 3, 5]],     # 05

    [-1, 0, [1, 3, 5]],     # 06
    [-1, 2, [1, 3, 5]],     # 07
    [-1, 4, [1, 3, 5]],     # 08
    [-1, 6, [1, 3, 5]],     # 09

    [0, 1, [1, 3, 5, 7]],  # 10
    [1, 3, [1, 3, 5, 7]],  # 11
    [2, 5, [1, 3, 5, 7]],  # 12
    [3, 7, [1, 3, 5, 7]],  # 13

    [-1, 0, [1, 3, 5, 7]],  # 14
    [-1, 2, [1, 3, 5, 7]],  # 15
    [-1, 4, [1, 3, 5, 7]],  # 16
    [-1, 6, [1, 3, 5, 7]],  # 17
    [-1, 8, [1, 3, 5, 7]]]  # 18

if __name__ == "__main__":
    # Run program
    the_ringer()
