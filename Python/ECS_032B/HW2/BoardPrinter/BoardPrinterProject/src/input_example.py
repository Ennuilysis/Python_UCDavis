from typing import List


# some example functions that use input
# to demonstrate how to test them in
# test/test_input_examples

def add2numbers_from_user() -> int:
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    return a + b


def multi_line_gatherer() -> List:
    num_lines = int(input('How many lines will you enter: '))
    lines = []
    for i in range(num_lines):
        line = input(f'Enter line {i}: ')
        lines.append(line)
    return lines
