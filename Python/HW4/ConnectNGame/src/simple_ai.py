from typing import List, TYPE_CHECKING
from ConnectNGame.src import move
from ConnectNGame.src import random_ai
from ConnectNGame.src.board import Board

if TYPE_CHECKING:
    from ConnectNGame.src import game


class SimpleAi(random_ai.RandomAi):
    @classmethod
    def get_valid_name(cls, players: List["Player"], case_matters: bool = False) -> str:
        return f'SimpleAi {len(players) + 1}'

    def get_move(self, game: "game.Game", the_board: Board) -> "move.Move":
        cols: int = the_board.num_cols
        for column in range(cols):
            if not the_board.is_column_full(column):
                boss = the_board.add_piece_to_column(self.piece, column)
                win:bool = game.is_part_of_win(boss, column)
                the_board.remove_piece_from_column(self.piece, column)
                if win:
                    return move.Move(self, column)
        for column in range(cols):
            if not the_board.is_column_full(column):
                boss = the_board.add_piece_to_column(self.opponent.piece, column)
                win:bool = game.is_part_of_win(boss, column)
                the_board.remove_piece_from_column(self.opponent.piece, column)
                if win:
                    return move.Move(self, column)

        return super().get_move(game, the_board)