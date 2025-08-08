"""
Unit tests for the TicTacToe game logic.

This module contains comprehensive tests for the TicTacToe class,
covering all game functionality including move validation, win detection,
draw scenarios, and state management.
"""

import unittest
from game import TicTacToe

class TestTicTacToe(unittest.TestCase):
    """
    Test suite for the TicTacToe game class.
    
    Tests cover:
    - Initial game state validation
    - Move execution and player switching
    - Invalid move handling
    - Win condition detection
    - Draw game scenarios
    """

    def test_initial_state(self):
        """Test that a new game has the correct initial state."""
        game = TicTacToe()
        self.assertEqual(game.current, 'X')
        self.assertIsNone(game.winner)
        self.assertEqual(game.board, [['', '', ''], ['', '', ''], ['', '', '']])

    def test_make_move_and_switch(self):
        """Test that moves are made correctly and players switch turns."""
        game = TicTacToe()
        self.assertTrue(game.make_move(0, 0))
        self.assertEqual(game.board[0][0], 'X')
        self.assertEqual(game.current, 'O')
        self.assertTrue(game.make_move(1, 1))
        self.assertEqual(game.board[1][1], 'O')
        self.assertEqual(game.current, 'X')

    def test_invalid_move(self):
        """Test that invalid moves (occupied cells) are rejected."""
        game = TicTacToe()
        game.make_move(0, 0)
        self.assertFalse(game.make_move(0, 0))  # Same spot

    def test_win(self):
        """Test win condition detection for a row win."""
        game = TicTacToe()
        game.make_move(0, 0)  # X
        game.make_move(1, 0)  # O
        game.make_move(0, 1)  # X
        game.make_move(1, 1)  # O
        self.assertIsNone(game.winner)
        game.make_move(0, 2)  # X wins with top row
        self.assertEqual(game.winner, 'X')

    def test_draw(self):
        """Test draw condition when board is full with no winner."""
        game = TicTacToe()
        # Create a specific draw scenario
        moves = [(0, 0), (0, 1), (0, 2),  # X, O, X
                 (1, 1), (1, 0), (1, 2),  # O, X, O  
                 (2, 1), (2, 0), (2, 2)]  # X, O, X
        for i, move in enumerate(moves):
            game.make_move(*move)
        self.assertEqual(game.winner, 'Draw')

if __name__ == '__main__':
    unittest.main()