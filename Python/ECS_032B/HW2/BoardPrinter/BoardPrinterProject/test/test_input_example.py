"""
Demo for how to use patch to override input's behavior
when testing
"""

import unittest,typing,numbers,copy
from ..src import board, boards_manager,input_example

# import patch, the function that we will use
# to replace the behavior of the normal input function
from unittest.mock import patch

from BoardPrinterProject.src.input_example import add2numbers_from_user, multi_line_gatherer

class TestInputExample(unittest.TestCase):
    def test_add2numbers_from_user(self):
        # put each line the "user" inputs as an element in a list
        user_input = ['5', '6']
        # the first parameter to patch is the path to the object you want to replace
        # so the below says to replace what the input function in BoardPrinterProject/src/input_example.py
        # returns with the values in our list, user_input
        with patch('BoardPrinterProject.src.input_example.input', side_effect=user_input):
            # inside the with statement the return values of input will be replaced
            # with what's in our list
            self.assertEqual(11, add2numbers_from_user())

    def test_multi_line_gatherer(self):
        # again we put each line of user input into our list
        user_input = ['3', 'hello', 'hi man', 'you can do this']
        # tell patch to replace what the input function in BoardPrinterProject/src/input_example.py
        # returns with the values in our list
        with patch('BoardPrinterProject.src.input_example.input', side_effect=user_input):
            lines = multi_line_gatherer()
            self.assertEqual(user_input[1:], lines)

    def test_multiple_calls_of_add2numbers_from_user(self):
        inputs_and_answers = [
            (['3', '-4'], -1),
            (['25', '-25'], 0),
            (['50', '40'], 90)
        ]
        for the_input, answer in inputs_and_answers:
            with patch('BoardPrinterProject.src.input_example.input', side_effect=the_input):
                with self.subTest(input=the_input):
                    total = add2numbers_from_user()
                    self.assertEqual(answer, total)


if __name__ == '__main__':
    unittest.main()
