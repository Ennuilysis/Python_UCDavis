from ConnectNGame.src import player, move
from ConnectNGame.src.board import Board
from typing import List, Set, TYPE_CHECKING
import random
if TYPE_CHECKING:
    from ConnectNGame.src import game


class RandomAi(player.Player):

    @classmethod
    def get_valid_piece(cls, players: List["Player"], blank_char: str, case_matters: bool = False) -> str:
        VISIBLE_CHARACTERS: List[str] = [chr(i) for i in range(ord('!'), ord('~') + 1)]
        illegal_pieces:Set[str] = {other_player.piece for other_player in players}
        illegal_pieces.add(blank_char)
        while True:
            piece_choice = random.choice(VISIBLE_CHARACTERS)
            if piece_choice not in illegal_pieces:
                return piece_choice

    @classmethod
    def get_valid_name(cls, players: List["Player"], case_matters: bool = False) -> str:
        return f'RandomAi {len(players) + 1}'

    def get_move(self, game:"game.Game", the_board: Board) -> "move.Move":
        not_full_columns:List[int] = [column for column in range(the_board.num_cols) if not the_board.is_column_full(column)]
        return move.Move(self, random.choice(not_full_columns))