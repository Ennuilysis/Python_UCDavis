import unittest
from ConnectNGame.src import move, game, player


class TestMove(unittest.TestCase):
    def test_from_string(self):
        test_player = player.Player('Bob', 'X')
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


    def test_make(self):
        ...

    def test_ends_game(self):
        ...


if __name__ == '__main__':
    unittest.main()
