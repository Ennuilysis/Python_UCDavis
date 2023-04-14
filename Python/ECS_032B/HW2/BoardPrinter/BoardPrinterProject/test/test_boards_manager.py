import unittest
from ..src import board, boards_manager,input_example

class TestBoardsManager(unittest.TestCase):
    def test_creates_board_list(self)->None:
        x=boards_manager.Board_manager()
        t=x.create_new_board_list(row=1,col=1,empty_symbol="J")
        J=[["J"]]
        self.assertEqual(t,J)
    def test_creates_save_key_and_save_dict(self)->None:
        x=boards_manager.Board_manager()
        self.assertEqual(x.save_key,[])

    def test_fill_spot(self) -> None:
        y=boards_manager.Board_manager()
        y.create_new_board(test=True,board_name="hello",row=1,col=1,empty_symbol="J",first_run=True)
        y.cur_board.Fill_spot(symbol="0", where=[0, 0], test=True)
        self.assertEqual(y.cur_board.board_list[0][0], "0")

    def test_erase_spot(self) -> None:
        x=boards_manager.Board_manager()
        x.create_new_board(test=True,board_name="hello",row=1,col=1,empty_symbol="J",first_run=True)
        x.cur_board.Fill_spot(symbol="O", where=[0, 0], test=True)
        x.cur_board.Erase_spot(0,0,check=1)
        self.assertEqual(x.cur_board.board_list[0][0], "J")

    def test_switch(self)->None:
        y = boards_manager.Board_manager()
        y.create_new_board(test=True, board_name="hello", row=1, col=1, empty_symbol="J", first_run=True)
        y.create_new_board(test=True, board_name="world", row=3, col=3, empty_symbol="III",first_run=False)
        y.create_new_board(test=True, board_name="die", row=4, col=3, empty_symbol="PP",first_run=False)
        y.switch_board(num=2)
        self.assertEqual(y.cur_board.board_name,"hello")

    def test_quit(self)-> None:

        x=boards_manager.Board_manager()
        x.program_quit()
        return Error # type: ignore




if __name__ == '__main__':
    unittest.main()

