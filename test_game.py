import unittest
from game import TicTacToe

class TestTicTacToe(unittest.TestCase):

    def test_initial_state(self):
        game = TicTacToe()
        self.assertEqual(game.current, 'X')
        self.assertIsNone(game.winner)
        self.assertEqual(game.board, [['', '', ''], ['', '', ''], ['', '', '']])

    def test_make_move_and_switch(self):
        game = TicTacToe()
        self.assertTrue(game.make_move(0, 0))
        self.assertEqual(game.board[0][0], 'X')
        self.assertEqual(game.current, 'O')
        self.assertTrue(game.make_move(1, 1))
        self.assertEqual(game.board[1][1], 'O')
        self.assertEqual(game.current, 'X')

    def test_invalid_move(self):
        game = TicTacToe()
        game.make_move(0, 0)
        self.assertFalse(game.make_move(0, 0))  # Same spot

    def test_win(self):
        game = TicTacToe()
        game.make_move(0, 0)  # X
        game.make_move(1, 0)  # O
        game.make_move(0, 1)  # X
        game.make_move(1, 1)  # O
        self.assertIsNone(game.winner)
        game.make_move(0, 2)  # X wins
        self.assertEqual(game.winner, 'X')

    def test_draw(self):
        game = TicTacToe()
        moves = [(0, 0), (0, 1), (0, 2),
                 (1, 1), (1, 0), (1, 2),
                 (2, 1), (2, 0), (2, 2)]
        for i, move in enumerate(moves):
            game.make_move(*move)
        self.assertEqual(game.winner, 'Draw')

if __name__ == '__main__':
    unittest.main()