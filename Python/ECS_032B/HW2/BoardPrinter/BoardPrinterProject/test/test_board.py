import unittest
from ..src import board


class TestBoard(unittest.TestCase):
    def test_fill_spot(self) -> None:
        y = board.Board( "k", 2, 2, "!")
        y.Fill_spot(symbol="0", where=[0, 0],test=True)
        self.assertEqual(y.board_list[0][0], "0")

    def test_erase_spot(self) -> None:
        y = board.Board("!", 2, 2, "!")
        y.Fill_spot(symbol="O", where=[0, 0], test=True)
        y.Erase_spot(0,0,check=1)
        self.assertEqual(y.board_list[0][0], "!")

    ...  # your tests for the board class


if __name__ == '__main__':
    unittest.main()
