from ConnectN.ConnectNGame.src import player, move
from ConnectN.ConnectNGame.src.board import Board
from ConnectN.ConnectNGame.src.player import Player
from typing import List, TYPE_CHECKING
import random



class RandomAi(player.Player):

    @classmethod
    def get_valid_piece(cls, players: List["Player"], blank_char: str, case_matters: bool = False) -> str:
        VISIBLE_CHARACTERS = [chr(i) for i in range(ord('!'), ord('~') + 1)]
        illegal_pieces = {other_player.piece for other_player in players}
        illegal_pieces.add(blank_char)
        while True:
            piece_choice = random.choice(VISIBLE_CHARACTERS)
            if piece_choice not in illegal_pieces:
                return piece_choice

    @classmethod
    def get_valid_name(cls, players: List["Player"], case_matters: bool = False) -> str:
        return f'RandomAi {len(players) + 1}'

    def get_move(self, game:"game.Game", the_board: Board) -> "move.Move":
        not_full_columns = [column for column in range(the_board.num_cols) if not the_board.is_column_full(column)]
        return move.Move(self, random.choice(not_full_columns))
