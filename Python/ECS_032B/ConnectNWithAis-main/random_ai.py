from ConnectNGame.src.players.player import Player
from ConnectNGame.src.board import Board
from typing import List, Tuple
import random, abc  # type: ignore


class RandomAi(Player):
    def __init__(self, player_number: int, players: List[Tuple[str, str, str]], board: Board):  # type: ignore
        self.name: str = "RandomAi " + str(player_number)
        self.piece: str = self.check_piece(players, board)
        self.player_num: int = player_number

    @staticmethod
    def create_player(player_num: int, players: List[Tuple[str, str, str]], board: Board) -> Player:  # type: ignore
        name_AI: str = "RandomAi " + str(player_num)
        globals()[name_AI] = RandomAi(player_num, players, board)
        return globals()[name_AI]

    def check_piece(self, players: List[Tuple[str, str, str]], board: Board) -> str:  # type: ignore
        VISIBLE_CHARACTERS: List[str] = [chr(i) for i in range(ord('!'), ord('~') + 1)]  # type: ignore
        y: List[str] = [t[1] for t in players]
        while True:
            piece: str = random.choice(VISIBLE_CHARACTERS)
            if piece == board.blank_character:
                continue
            elif piece in y:
                continue
            return piece

    def play(self, board: Board) -> int:
        cols: int = board.num_columns
        while True:
            col: int = random.choice(range(cols))
            x: List[str] = [row[col] for row in board.contents]
            if board.blank_character not in x:
                continue
            break
        return col

    @abc.abstractmethod
    def check_name_and_piece(self, player_num: int, players: List[Tuple[str, str, int]], board: Board) -> Tuple[str, str]:
        ...
