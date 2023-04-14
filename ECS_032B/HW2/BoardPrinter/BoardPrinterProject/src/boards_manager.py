# place your BoardsManager class in this file
from typing import List
from BoardPrinterProject.src import board


class Board_manager(board.Board):
    def __init__(self)->None :
        self.cur_board = None
        self.save_key: List[board.Board] = []
        self.board_id: int = 0

    def add_1_to_board_id(self) -> None:
        self.board_id += 1

    def save_board(self, board_object: board.Board) -> None:
        x = [t.__repr__() for t in self.save_key]
        if board_object.__repr__() not in x:
            self.save_key.insert(0, board_object)

    def program_quit(self) -> None:
        quit()

    def create_new_board(self, test=False, board_name=None, row=None,col=None,empty_symbol=None, first_run: bool = False) -> None:
        self.add_1_to_board_id()
        if test==False:
            board_name: str = input("Enter the name of your board: ") # type: ignore
            row: int = int(input("Enter the number of rows for your board: ")) # type: ignore
            col: int = int(input("Enter the number of columns for your board: ")) # type: ignore
            empty_symbol: str = input("Enter the blank character to be used on your board: ") # type: ignore
        board_id = board_name + str(self.board_id)
        globals()[board_id] = board.Board(board_name, row, col, empty_symbol)
        if first_run == True:
            self.cur_board = globals()[board_id]
        self.save_board(globals()[board_id])

    def switch_board(self,num=None) -> None:
        for j, i in enumerate(self.save_key):
            print(f'{j}. {i}')
        if num==None:
            num = int(input("Enter the number of the board you want to switch to: "))
        self.cur_board = self.save_key[num]  # type: ignore
