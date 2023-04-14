import unittest
from ..src import sorting
#keep imports

#del variable
#The above would delete the variable, including within a function, during the functions processing.
#.. is one directory
#. means current directory
#test valid example
#smallest
#make my own list for the test cases
#context of .src vs src, modules treat it different. Rules change in modules, modules are collections of files.

class TestSwap(unittest.TestCase):
    def test_swapping(self) -> None:
        """
        Check that swap is able to swap two values in a list
        And does not modify any of the other values besides the two that were swapped
        swap(values: List, index1: int, index2: int) -> None:
        """
        test_list = [1,2,3,4,5,6,7]
        test_list_swap_check=[1,5,3,4,2,6,7] #expected
        sorting.swap(test_list, 1, 4)
        self.assertEqual(test_list, test_list_swap_check, "The list did not correctly swap different indexes.")

        #make list of values. Call swap, on list, check if elements were swapped.
        #input should be list
        #answer and result should be same, swap at same places, ect.
        #ouput should be none.

    def test_swap_self(self) -> None:
        """
        Check that swap still works if index1 and index2 are the same.
        :return:
        """
        #input list
        #use same code as above, same list, but different answer. assertEqual.
        test_list = [1, 2, 3, 4, 5, 6, 7]
        test_list2 = [1,2,3,4,5,6,7]
        sorting.swap(test_list, 2, 2)
        self.assertEqual(test_list, test_list2, "The list did not correctly swap identical indexes.")


if __name__ == '__main__':
    unittest.main()