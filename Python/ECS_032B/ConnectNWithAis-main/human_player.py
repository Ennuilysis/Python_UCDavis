import abc
from ConnectNGame.src.player import Player
from ConnectNGame.src.board import Board
from typing import List, Tuple


class HumanPlayer(Player):
    # creates human player instances

    def __init__(self, player_number: int, players: List[Tuple[str, str, int]], board: Board):
        self.name = None
        self.piece = None
        self.player_num = player_number
        self.check_name_and_piece(player_number, players, board)
        return

    @staticmethod
    def create_player(player_num: int, players: List[Tuple[str, str, int]], board: Board) -> Player:
        globals()["HumanPlayer " + str(player_num)] = HumanPlayer(player_num, players, board)
        return (globals()["HumanPlayer " + str(player_num)])

    @abc.abstractmethod
    def check_name_and_piece(self, player_num: int, players: List[Tuple[str, str, int]], board: Board) -> None:
        x = [t[0] for t in players]
        x = [t.lower() for t in x]
        y = [t[1] for t in players]
        while True:
            player_name = input(f"HumanPlayer {player_num} enter your name: ")
            player_name = player_name.replace(" ", "")
            # print(f"Player_name {player_name}")
            player_name_lower = player_name.lower()
            if len(player_name) == 0:
                print("Your name cannot be the empty string or whitespace")
                continue
            elif player_name_lower in x:
                print(f'You cannot use {player_name} for your name as someone else is already using it.')
                continue

            piece:str = input(f"HumanPlayer {self.player_num} enter your piece: ")
            piece:str = piece.replace(" ", "")
            if len(piece) == 0:
                print("Your piece cannot be the empty string or whitespace")
                continue
            elif len(piece) > 1:
                print(f'{piece} is not a single character. Your piece can only be a single character.')
                continue
            elif piece == board.blank_character:
                print('Your piece cannot be the same as the blank character.')
                continue
            elif piece in y:
                pos = y.index(piece)
                print(f'You cannot use {piece} for your piece as {players[pos][0]} is already using it.')
                continue
            else:
                break
        self.name: str = player_name
        self.piece: str = piece

    def play(self, board: Board) -> int:
        col = board.num_columns

        while True:
            try:
                pos1 = input(f"{self.name}, please enter the column you want to play in: ")
                pos = int(pos1)
            except:
                print(f'{self.name}, column needs to be an integer. {pos1} is not an integer. ')  # type: ignore
                continue
            if pos > col - 1 or pos < 0:
                print(f'Your column needs to be between 0 and {col - 1} but is actually {pos}.')  # type: ignore
                continue
            x: List[str] = [t[pos] for t in board.contents]
            if board.blank_character not in x:
                print(f'You cannot play in {pos} because it is full.')
                continue
            break
        return pos
