import unittest, copy
from unittest.mock import patch
from ConnectN.ConnectNGame.test.print_capturer import PrintCapturer
from ConnectN.ConnectNGame.src.board import Board, ColumnFullError, ColumnOutOfBoundsError, EmptySpotError
from ConnectN.ConnectNGame.src import move
from ConnectN.ConnectNGame.src.random_ai import RandomAi
from ConnectN.ConnectNGame.src.simple_ai import SimpleAi
from ConnectN.ConnectNGame.src.player import Player
from ConnectN.ConnectNGame.src.human_player import HumanPlayer
from ConnectN.ConnectNGame.src.game import Game

Player_Type_List = [Player, RandomAi, SimpleAi, HumanPlayer]


class Test(unittest.TestCase):

    def test_num_rows(self):
        the_board = Board(3, 5, '*')
        self.assertEqual(3, the_board.num_rows)

    # Good
    def test_num_cols(self):
        the_board = Board(3, 5, '*')
        self.assertEqual(5, the_board.num_cols)

    # Good

    def test_is_full(self):
        the_board = Board(3, 5, '*')
        self.assertFalse(the_board.is_full)
        the_board.contents = [['X'] * 5] * 3
        self.assertTrue(the_board.is_full)
        the_board.contents[1][1] = '*'
        self.assertFalse(the_board.is_full)

    # Good

    def test_is_column_in_bounds(self):
        the_board = Board(3, 5, '*')
        for i in range(-10, 10):
            with self.subTest(col=i):
                self.assertEqual(0 <= i < 5, the_board.is_column_in_bounds(i))

    # Good

    def test_contains_blank_char(self):
        the_board = Board(3, 2, '*')
        the_board.contents = [['*', 'X'],
                              ['O', '*'],
                              ['*', 'J']]
        with self.subTest(msg='Should Contain Blanks'):
            self.assertTrue(the_board.contains_blank_character(0, 0))
            self.assertTrue(the_board.contains_blank_character(1, 1))
            self.assertTrue(the_board.contains_blank_character(2, 0))

        with self.subTest(msg='Should NOT Contain Blanks'):
            self.assertFalse(the_board.contains_blank_character(0, 1))
            self.assertFalse(the_board.contains_blank_character(1, 0))
            self.assertFalse(the_board.contains_blank_character(2, 1))

    # Good

    def test_add_piece_to_column(self):
        the_board = Board(5, 6, '*')
        answer_contents = copy.deepcopy(the_board.contents)
        answer_heights = copy.deepcopy(the_board._number_of_pieces_in_columns)
        pieces_added = 0
        piece_to_add = 'X'
        for row in range(the_board.num_rows):
            for col in range(the_board.num_cols):
                with self.subTest(row=row, col=col, pieces_added=pieces_added):
                    the_board.add_piece_to_column(piece_to_add, col)
                    answer_contents[row][col] = piece_to_add
                    answer_heights[col] += 1
                    self.assertEqual(answer_contents, the_board.contents)
                    self.assertEqual(answer_heights, the_board._number_of_pieces_in_columns)
                    pieces_added += 1
        for col in range(the_board.num_cols):
            with self.subTest(col=col, msg='Play in full column'):
                self.assertRaises(ColumnFullError, the_board.add_piece_to_column, 'X', col)
        for col in [-5, -3, -1, 10, 50, 6]:
            with self.subTest(col=col, msg='Play out of bounds'):
                self.assertRaises(ColumnOutOfBoundsError, the_board.add_piece_to_column, 'X', col)

    # Good

    def test_count_matches_horizontally(self):
        the_board = Board(4, 4, '*')
        the_board.contents = [['X', 'X', 'X', 'X'],
                              ['O', 'O', 'X', 'X'],
                              ['O', 'O', '*', 'X'],
                              ['O', '*', '*', 'O']]
        answers = [[4, 4, 4, 4],
                   [2, 2, 2, 2],
                   [2, 2, None, 1],
                   [1, None, None, 1]]
        for row_index, row in enumerate(answers):
            for col_index, count in enumerate(row):
                if count is not None:
                    with self.subTest(row=row_index, col=col_index):
                        self.assertEqual(count, the_board.count_matches_horizontally(row_index, col_index))

    # Good

    def test_count_matches_vertically(self):
        the_board = Board(4, 4, '*')
        the_board.contents = [['X', 'X', 'X', 'X'],
                              ['O', 'O', 'X', 'X'],
                              ['O', 'O', '*', 'X'],
                              ['O', '*', '*', 'O']]
        answers = [[1, 1, 2, 3],
                   [3, 2, 2, 3],
                   [3, 2, None, 3],
                   [3, None, None, 1]]

        for row_index, row in enumerate(answers):
            for col_index, count in enumerate(row):
                if count is not None:
                    with self.subTest(row=row_index, col=col_index):
                        self.assertEqual(count, the_board.count_matches_vertically(row_index, col_index))

    # Good

    def test_count_matches_in_right_diagonal_win(self):
        the_board = Board(4, 4, '*')
        the_board.contents = [['X', 'X', 'X', 'X'],
                              ['O', 'O', 'X', 'X'],
                              ['O', 'O', '*', 'X'],
                              ['O', '*', '*', 'O']]
        answers = [[1, 1, 1, 2],
                   [1, 2, 2, 1],
                   [2, 2, None, 1],
                   [2, None, None, 1]]
        for row_index, row in enumerate(answers):
            for col_index, count in enumerate(row):
                if count is not None:
                    with self.subTest(row=row_index, col=col_index):
                        self.assertEqual(count, the_board.count_matches_in_right_diagonal(row_index, col_index))

    # Good

    def test_count_matches_in_left_diagonal(self):
        the_board = Board(4, 4, '*')
        the_board.contents = [['X', 'X', 'X', 'X'],
                              ['O', 'O', 'X', 'X'],
                              ['O', 'O', '*', 'X'],
                              ['O', '*', '*', 'O']]
        answers = [[1, 3, 2, 1],
                   [2, 1, 3, 2],
                   [1, 2, None, 3],
                   [1, None, None, 1]]

        for row_index, row in enumerate(answers):
            for col_index, count in enumerate(row):
                if count is not None:
                    with self.subTest(row=row_index, col=col_index):
                        self.assertEqual(count, the_board.count_matches_in_left_diagonal(row_index, col_index))

    # Good

    def test_iter(self):
        the_board = Board(4, 4, '*')
        the_board.contents = [['X', 'X', 'X', 'X'],
                              ['O', 'O', 'X', 'X'],
                              ['O', 'O', '*', 'X'],
                              ['O', '*', '*', 'O']]
        for answer, value in zip(the_board, the_board.contents):
            self.assertEqual(answer, value)

    # Good

    def test_column_iterate(self):
        the_board = Board(4, 4, '*')
        the_board.contents = [['X', 'X', 'X', 'X'],
                              ['O', 'O', 'X', 'X'],
                              ['O', 'O', '*', 'X'],
                              ['O', '*', '*', 'O']]
        columns = [['X', 'O', 'O', 'O'],
                   ['X', 'O', 'O', '*'],
                   ['X', 'X', '*', '*'],
                   ['X', 'X', 'X', 'O']]

        for answer, value in zip(columns, the_board.column_iterate()):
            self.assertSequenceEqual(answer, value)
    #All Board Gooe
    # Good

    Player_Type_List = [Player, RandomAi, SimpleAi, HumanPlayer]
    #Player types
    def test_from_string(self):
        test_player = Player('Bob', 'X')
        invalid_moves = ['hi', '1.2', '3 5']
        for bad_move in invalid_moves:
            with self.subTest(move=bad_move):
                self.assertRaises(move.MoveFormatError, move.Move.from_string, test_player, bad_move)

        valid_moves = ['2', '3', '1']
        for valid_move in valid_moves:
            with self.subTest(move=valid_move):
                answer = move.Move(test_player, int(valid_move))
                test_move = move.Move.from_string(test_player, valid_move)
                self.assertEqual(answer, test_move)

    def setUp(self) -> None:
        self.other_players = [Player('Bob', 'X'), Player('Sally', 'O')]
        self.board = Board(4, 5, '#')

    def test_get_valid_piece(self):
        blank_char = self.board.blank_char
        inputs_and_answers = [
            ([''], 'Your piece cannot be the empty string or whitespace.'),
            (['   \t \t \t     \n'], 'Your piece cannot be the empty string or whitespace.'),
            (['X is a great choice'],
             f'X is a great choice is not a single character. Your piece can only be a single character.'),
            ([blank_char], 'Your piece cannot be the same as the blank character.'),
            (['x'], 'You cannot use x for your piece as Bob is already using it.'),
            (['o'], 'You cannot use o for your piece as Sally is already using it.')
        ]

        for user_input, error_msg in inputs_and_answers:
            with self.subTest(user_input=user_input):
                with patch('ConnectN.ConnectNGame.src.player.input', side_effect=user_input):
                    self.assertRaisesRegex(ValueError, error_msg,
                                           Player.get_valid_piece, self.other_players, blank_char)
        user_input = ['L']
        with self.subTest(user_input=user_input):
            with patch('ConnectN.ConnectNGame.src.player.input', side_effect=user_input):
                piece = Player.get_valid_piece(self.other_players, blank_char)
                self.assertEqual(user_input[0], piece)

    def test_get_valid_name(self):
        inputs_and_answers = [
            ([''], 'Your name cannot be the empty string or whitespace.'),
            (['   \t \t \t     \n'], 'Your name cannot be the empty string or whitespace.'),
            (['boB'], 'You cannot use boB for your name as someone else is already using it.'),
            (['SaLlY'], 'You cannot use SaLlY for your name as someone else is already using it.')
        ]

        for user_input, error_msg in inputs_and_answers:
            with self.subTest(user_input=user_input):
                with patch('ConnectNGame.src.player.input', side_effect=user_input):
                    self.assertRaisesRegex(ValueError, error_msg,
                                           Player.get_valid_name, self.other_players)

        user_input = ['bobert', 'sal', 'bo', 'joe']
        with patch('ConnectNGame.src.player.input', side_effect=user_input):
            for name in user_input:
                with self.subTest(name=name):
                    received_name = Player.get_valid_name(self.other_players)
                    self.assertEqual(name, received_name)

    def test_create_from_user_input(self):
        user_input = ['', '  ', 'Bob', 'Joe', '', 'Joe', ' ', 'Mike', 'o', 'Mike', self.board.blank_char, 'Wally',
                      'W']
        capture = PrintCapturer()
        print_output = ['Your name cannot be the empty string or whitespace.\n',
                        'Your name cannot be the empty string or whitespace.\n',
                        'You cannot use Bob for your name as someone else is already using it.\n',
                        'Your piece cannot be the empty string or whitespace.\n',
                        'Your piece cannot be the empty string or whitespace.\n',
                        'You cannot use o for your piece as Sally is already using it.\n',
                        'Your piece cannot be the same as the blank character.\n']
        answer_player = Player(*user_input[-2:])
        with patch('ConnectNGame.src.player.Player.input', side_effect=user_input):
            with patch('ConnectNGame.src.player.Player.print', side_effect=capture):
                new_player = Player.create_from_user_input(self.other_players, self.board.blank_char)
                self.assertEqual(answer_player, new_player)
                self.assertEqual(print_output, capture.output)

    def test_take_turn(self):
        ...

    def test_get_move(self):
        user_input = ['2']
        test_player = ('George', 'P')
        answer = move.Move(test_player, 2)
        with patch('ConnectNGame.src.player.input', side_effect=user_input):
            user_move = test_player.get_move()
            self.assertEqual(answer, user_move)

    if __name__ == '__main__':
        unittest.main()

    def test_make(self):
        ...

    def test_ends_game(self):

    def test_valid_player(self):
        # def get_valid_player_type(player_num: int) -> type:
        input_list = ["RaN", "HuM", "simpl", "human", "RandomAi"]
        Anser = [RandomAi, HumanPlayer,SimpleAi,HumanPlayer,RandomAi]
        for x in enumerate(input_list):
            with patch("ConnectNGame.src.game.input", side_effect=x):
                thing = game.get_valid_player_type()

        ...


if __name__ == '__main__':
    unittest.main()
