from ConnectNGame.src.player import Player
from ConnectNGame.src.players.random_ai import RandomAi
from ConnectNGame.src.board import Board
from typing import Tuple, List
import random


class SimpleAI(RandomAi):
    def __init__(self, player_num: int, players: List[Tuple[str, str, str]], board: Board):  # type: ignore
        super().__init__(player_num, players, board)
        self.name: str = "SimpleAi " + str(player_num)

    @staticmethod
    def create_player(player_num: int, players: List[Tuple[str, str, str]], board: Board, Test: bool = False) -> RandomAi:
        name = "SimpleAI " + str(player_num)
        globals()[name] = SimpleAI(player_num, players, board)
        return (globals()[name])

    def win_check(self, piece, board) -> Tuple[int]:
        board_list: List[List[str]] = board.contents
        longest_vect = 0

        def check_next(row: int, col: int, row_chng: int, col_chng: int) -> int:
            if row == -1 or col == -1:
                return 0
            try:
                next_chr: str = board_list[row][col]
            except IndexError:
                return 0
            if next_chr == piece:
                return 1 + check_next(row + row_chng, col + col_chng, row_chng, col_chng)
            else:
                return 0

        for col in range(board.num_columns):
            for row in range(board.num_rows):
                if piece == board.contents[row][col]:
                    up_vect: int = check_next(row, col, -1, 0)
                    top_right_vect: int = check_next(row, col, 1, 1)
                    right_vect: int = check_next(row, col, 0, 1)
                    bottom_right_vect: int = check_next(row, col, -1, 1)
                    longest_vect: int = max(up_vect, top_right_vect, right_vect, bottom_right_vect, longest_vect)
        if longest_vect >= board.pieces_to_win:
            return True
        else:
            False

    def play(self, board: Board, Test: bool = False):
        col = board.num_columns
        for column in range(col):
            cord = board.drop_piece_into_column(column, self.piece, cheat=True)
            win = self.win_check(self.piece, board)
            correct_row_cord=board.num_rows-cord[0]-1
            board.fill_spot(correct_row_cord, cord[1], board.blank_character)
            if win:
                return column
        for column in range(board.num_columns):
            cord = board.drop_piece_into_column(column, self.piece, cheat=True)
            correct_row_cord = board.num_rows - cord[0] - 1
            win = self.win_check(self.piece, board)
            board.fill_spot( correct_row_cord, cord[1], board.blank_character)
            if win:
                return column
        while True:
            pos = random.choice(range(col))
            x: List[str] = [t[pos] for t in board.contents]
            if board.blank_character not in x:
                continue
            break
        return pos
