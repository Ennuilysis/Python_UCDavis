from ConnectNGame.src.board import Board
from ConnectNGame.src.player import Player
from ConnectNGame.src.players.human_player import HumanPlayer
from ConnectNGame.src.players.random_ai import RandomAi
from ConnectNGame.src.players.simple_ai import SimpleAI

from ConnectNGame.src.config import Config
from typing import List, Tuple, Union
import random


class Game(object):
    def __init__(self, game_config: Config):
        self.players: List[Tuple[str, str, int]] = []  # name, piece, number
        self.board: Board = Board.build_board_from_config(game_config)
        self.Player_instants: List[Union[HumanPlayer, SimpleAI, RandomAi]] = []
        self.player_num = 0

    def check_type(self) -> str:
        while True:
            print(f"Choose the type for Player {self.player_num}")
            P_type = input(f"Enter Human or Random or Simple: ")
            thang = ['human', 'random', 'simple']
            thangy = []
            try:
                P_type = P_type.strip().lower()
                if P_type == "":
                    raise TypeError
            except:  # type: ignore
                print(f'{P_type} is not one of Human or Random or Simple. Please try again.')
                continue
            ting = len(P_type)
            for x in thang:
                thangy.append(x[0:ting])
            try:
                thangy.index(P_type)
            except:  # type: ignore
                print(f'{P_type} is not one of Human or Random or Simple. Please try again.')
                continue
            # print(thang[thangy.index(P_type)])
            return thang[thangy.index(P_type)]

    def play(self)->None:
        while True:
            self.player_num += 1
            type_choice:str = self.check_type()
            type_choices = {"random": RandomAi, "human": HumanPlayer, "simple": SimpleAI}
            self.Player_instants.append(type_choices[type_choice].create_player(player_num =self.player_num, players=self.players,board=self.board))
            x = self.Player_instants[-1]
            self.players.append((x.name, x.piece, x.player_num))
            self.player_num += 1
            type_choice = self.check_type()
            self.Player_instants.append(type_choices[type_choice].create_player(player_num=self.player_num, players=self.players,board=self.board))
            x = self.Player_instants[-1]
            self.players.append((x.name, x.piece, x.player_num))
            print(self.board)
            while True:
                for x in self.Player_instants:
                    play_col: int = x.play(self.board)  # type: ignore
                    self.board.drop_piece_into_column(play_col, x.piece)
                    print(self.board)
                    win: bool = self.win_check(x.piece, x.name)
                    if win:
                        print(f"{x.name} won the game!")
                        quit()
                    if self.board.is_full():
                        print("Tie Game.")
                        quit()

    def win_check(self, piece, name) -> bool:
        board_list: List[List[str]] = self.board.contents
        longest_vect = 0

        def check_next(row: int, col: int, row_chng: int, col_chng: int) -> int:
            if row == -1 or col == -1:
                return 0
            try:
                next_chr: str = board_list[row][col]
            except IndexError:
                # print("problem")
                return 0
            if next_chr == piece:
                # print("{}", row, col, next_chr)
                return 1 + check_next(row + row_chng, col + col_chng, row_chng, col_chng)
            else:
                return 0

        for col in range(self.board.num_columns):
            for row in range(self.board.num_rows):
                if piece == self.board.contents[row][col]:
                    # print("{}", row, col)
                    up_vect: int = check_next(row, col, -1, 0)
                    # print("topright")
                    top_right_vect: int = check_next(row, col, 1, 1)
                    right_vect: int = check_next(row, col, 0, 1)
                    bottom_right_vect: int = check_next(row, col, -1, 1)
                    # print("!!!!",up_vect,top_right_vect,right_vect,bottom_right_vect)
                    longest_vect: int = max(up_vect, top_right_vect, right_vect, bottom_right_vect, longest_vect)
                    # print("?????",longest_vect)
        if longest_vect >= self.board.pieces_to_win:
            print(f"{name} won the game!")
            quit()

        return False
