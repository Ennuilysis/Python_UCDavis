import abc
from typing import Any, List, Optional, TYPE_CHECKING
from . import move
from .board import Board, BoardError
if TYPE_CHECKING:
    from ConnectNGame.src import game


class Player(abc.ABC):
    @classmethod
    def create_for_game(cls, players: List["Player"], blank_char: str) -> "Player":
        """
        Create player for user input
        :param players: The other players in the game
        :param blank_char: The blank character in the board
        :return: A player created from this user's input
        """
        while True:
            try:
                name = cls.get_valid_name(players)
                piece = cls.get_valid_piece(players, blank_char)
                return cls(name, piece)
            except ValueError as error:
                print(error)

    @classmethod
    @abc.abstractmethod
    def get_valid_piece(cls, players: List["Player"], blank_char: str, case_matters: bool = False) -> str:
        """
        Check if piece is a valid one to use in the current game.
        A piece is valid if it is 1 character big
        and no other players are using it.
        :param players: The other players in the game
        :param blank_char: The blank character for the board
        :param case_matters: Does case matter when comparing pieces?
        :return: the piece the player has chosen
        :raises ValueError if the piece is not valid
        """
        ...

    @classmethod
    @abc.abstractmethod
    def get_valid_name(cls, players: List["Player"], case_matters: bool = False) -> str:
        """
        Check if name is a valid name for this player
        :param players:  The other players in the game
        :param case_matters: Whether capitalization matters or not
        :return: The name the user has chosen
        :raises: ValueError if the name chosen is not vlaid

        """
        ...

    def __init__(self, name: str, piece: str, opponent: Optional["Player"] = None) -> None:
        self.name = name
        self.piece = piece
        self.opponent = opponent

    def take_turn(self, game: "game.Game", the_board: Board) -> "move.Move":
        """
        Have the player take their turn
        :param the_board: the board to make their move on
        :return: the move the player made
        """
        while True:
            try:
                player_move = self.get_move(game, the_board)
                player_move.make(the_board)
            except (move.MoveError, BoardError) as error:
                print(error)
            else:
                return player_move

    @abc.abstractmethod
    def get_move(self, game: "game.Game", the_board: Board) -> "move.Move":
        """
        Get a move from the user
        :return: the move the user made
        :raises: MoveError if the move is invalid
        """
        ...

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Player) and \
               self.name == other.name and \
               self.piece == other.piece

    def __ne__(self, other: Any) -> bool:
        return not self == other
