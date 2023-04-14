import abc
from typing import List, Tuple
from ConnectNGame.src.board import Board


class Player(object):
    @abc.abstractmethod
    def __init__(self, player_number: int, players: List[Tuple[str, str, int]], board: Board):
        self.name = None
        self.piece = None
        self.player_num = player_number
        self.check_name_and_piece(player_number, players, board)

    @abc.abstractmethod
    def create_player(self, player_num: int, players: List[Tuple[str, str, int]], board: Board) -> object:
        globals()[self.name] = Player(player_num, players)
        return (globals()[self.name])

    @abc.abstractmethod
    def check_name_and_piece(self, player_num: int, players: List[Tuple[str, str, int]], board: Board) -> Tuple[
        str, str]:
        ...

    @abc.abstractmethod
    def play(self, board):
        ...
