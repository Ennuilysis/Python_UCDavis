import unittest
from ..src import sorting
#keep imports



class TestFindMinIndex(unittest.TestCase):
    def test_find_min_index(self) -> None:
        """
        Check if find min index works correctly when
        searching the entire list
        """
        test_list=[10,11,8,12,13]
        ans_index=2
        result_index=sorting.get_index_of_min_item(test_list)
        self.assertEqual(ans_index,result_index)


    def test_find_min_index_not_starting_at_front_of_array(self) -> None:
        """
        Check if find min index works correctly when starting at an element
        that is not the first element in the list.
        :return:
        """

    def test_input_list_is_not_modified(self)->None:
        """
        Check that find_min_index does not modify the list passed to it
        :return:
        """


if __name__ == '__main__':
    unittest.main()
