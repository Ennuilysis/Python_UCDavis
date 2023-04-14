# Place your Board class in this file
from typing import List, Union
import typing


class Board:
    board_name: str
    row: int
    col: int
    empty_symbol: str
    board_list: List[List[str]]

    def create_new_board_list(self, row: int, col: int, empty_symbol: str) -> List[List[str]]:
        cur_board_list: List[List[str]] = []
        for i in range(row):
            cur_board_list.append([])
            for j in range(col):
                cur_board_list[i].append(empty_symbol)
        return cur_board_list

    def __init__(self, board_name: str, row: int, col: int, empty_symbol: str,
                 board_list: List[List[str]] = [["DIE"]]) -> None:
        self.board_name: str = board_name
        self.row: int = int(row)
        self.col: int = int(col)
        self.empty_symbol: str = empty_symbol
        self.board_list = self.create_new_board_list(self.row, self.col, self.empty_symbol)

    def Fill_spot(self, symbol: str=None, where: List[int]=None, test = False ) -> None:
        if test==False:
            symbol = input("Enter the character you want to add to the board: ")
            whereD = input("Enter the position to place the character in the form row,col: ")
            whereD = whereD.strip('"')
            where = whereD.split(",")
        row, col = int(where[0]), int(where[1])
        self.board_list[row][col] = symbol

    def Erase_spot(self, row: int = 0, col: int = 0, check: int = 0) -> None:
        if check == 0:
            whereK = input("Enter the position you want to erase in the form row,col: ")
            where = whereK.split(",")
            row, col = int(where[0]), int(where[1])
        self.board_list[row][col]: str = self.empty_symbol  # type: ignore

    def __str__(self):
        return self.board_name
