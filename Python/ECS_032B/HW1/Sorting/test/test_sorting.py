import unittest
from typing import TypeVar
from  ..src import sorting
T = TypeVar('T')
#keep imports
#rather use same list across files. Keep it simple.
x=(1 for i in range(10))
print(x)

class TestSorting(unittest.TestCase):
    def test_sorting_empty_list(self) -> None:
        """
        Check that we can sort the empty list correctly.
        :return:
        """
        #create empty list, sorting an empty list should result in empty list, or None.
        values_empty = []
        sorting.sort_items(values_empty)
        sorted_empty_values = []
        self.assertEqual(values_empty, sorted_empty_values, "Cant sort empty lists.")

    def test_already_sorted(self) -> None:
        """
        Check that we can sort a list that is already sorted
        :return:
        """
        test_list=[1,2,3,4,5,6]
        sorting.sort_items(test_list)
        #self.assertRaises(IndexError, "The sorting program was unable to complete.")
        self.assertSequenceEqual(test_list,[1,2,3,4,5,6])

    def test_reverse_sorted(self) -> None:
        """
        Check that we can sort a list that is in reverse sorted order
        :return:
        """
        test_reverse=[6,5,4,3,2,1]
        answer_test=[1,2,3,4,5,6]
        sorting.sort_items(test_reverse)
        self.assertSequenceEqual(test_reverse,answer_test, "The module is unable to correctly sort reverse sorted lists.")


    def test_average_case(self) -> None:
        """
        Check that we can sort an "average" list of unsorted values
        :return:
        """
        test_list=[9,23,44,31,33,29]
        answer=[9,23,29,31,33,44]
        sorting.sort_items(test_list)

        self.assertListEqual(test_list, answer)
        #create list of random numbers


    def test_sort_strings(self) -> None:
        """
        Test sorting a tuple of strings.
        :return:
        """
        #You cannot sort tuples. Tuples are immutable.
        test_tuple=("Apple","Bannana","Cucumber","Date")

    def test_sorting_dictionary_keys(self) -> None:
        """
        Test sorting a dictionary where the keys are Tuple[str, int] and the values are
        int
        :return:
        """
        a=("Apple","Bannana","Cucumber","Date")
        b=(1,4,2,3)
        #when iterating through dictionary, the for loop only iterates through keys
        test_tuple_dict=dict(a,b)

    def test_sort_set(self) -> None:
        """
        Test sorting a set of values
        :return:
        """
        #type is set

    def test_sort_generator(self) -> None:
        """
        Check that we can correctly sort values coming from a generator
        :return:
        """
        #generators are their own type.
        #iterate through generator to create list.

    def test_input_does_not_change(self) -> None:
        """
        Check that the iterable passed to sort_items does not modify its input
        :return:
        """
        #Has to create a new object, or use new memory. It doesn't mutate original.

    def test_new_list_returned(self) -> None:
        """
        Check that the list that sort_items returns is a new list
        i.e. the list returned by sort_items IS not the same as the parameter passed to it
        :return:
        """

    def test_random(self):
        """
        Test sorting randomly generated lists of numbers.
        Use the random module to generate at least 10 different lists of numbers
        and see that they are sorted correctly. Testing that each list is correct should
        be done within a subTest. To ensure that the randomly generated lists are the
        same each time you generate them, make sure to first seed the random number generator
        first. This can be done by doing random.seed(number). For example, random.seed(17).
        Also don't forget that you will need to import the random module to be able to use it.
        :return:
        """

if __name__=="__main__":
    unittest.main