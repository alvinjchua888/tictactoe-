class TicTacToe:
    """
    A Tic-Tac-Toe game implementation.
    
    This class manages the game state, validates moves, checks for win conditions,
    and handles game logic for a standard 3x3 Tic-Tac-Toe game.
    
    Attributes:
        board (list): 3x3 list representing the game board, with empty strings for empty cells
        current (str): Current player ('X' or 'O')
        winner (str): Winner of the game ('X', 'O', 'Draw', or None if game is ongoing)
    """
    
    def __init__(self, board=None, current='X', winner=None):
        """
        Initialize a new Tic-Tac-Toe game.
        
        Args:
            board (list, optional): 3x3 list representing an existing board state.
                                  If None, creates an empty board.
            current (str, optional): Current player ('X' or 'O'). Defaults to 'X'.
            winner (str, optional): Winner of the game. Defaults to None.
        """
        self.board = board if board else [['' for _ in range(3)] for _ in range(3)]
        self.current = current
        self.winner = winner

    def make_move(self, row, col):
        """
        Attempt to make a move at the specified position.
        
        Args:
            row (int): Row index (0-2) for the move
            col (int): Column index (0-2) for the move
            
        Returns:
            bool: True if the move was successful, False if invalid
            
        Note:
            A move is invalid if:
            - The cell is already occupied
            - The game has already ended (winner exists)
        """
        if self.board[row][col] or self.winner:
            return False
        
        self.board[row][col] = self.current
        
        if self.check_win(self.current):
            self.winner = self.current
        elif self.is_draw():
            self.winner = 'Draw'
        else:
            # Switch to the other player
            self.current = 'O' if self.current == 'X' else 'X'
        
        return True

    def check_win(self, player):
        """
        Check if the specified player has won the game.
        
        Args:
            player (str): Player to check for win ('X' or 'O')
            
        Returns:
            bool: True if the player has won, False otherwise
            
        Note:
            Checks all possible win conditions:
            - Three in a row (any row)
            - Three in a column (any column)
            - Three in the main diagonal (top-left to bottom-right)
            - Three in the anti-diagonal (top-right to bottom-left)
        """
        b = self.board
        
        # Check rows and columns
        for i in range(3):
            if all(b[i][j] == player for j in range(3)):  # Check row i
                return True
            if all(b[j][i] == player for j in range(3)):  # Check column i
                return True
        
        # Check main diagonal (top-left to bottom-right)
        if all(b[i][i] == player for i in range(3)):
            return True
        
        # Check anti-diagonal (top-right to bottom-left)
        if all(b[i][2-i] == player for i in range(3)):
            return True
        
        return False

    def is_draw(self):
        """
        Check if the game has ended in a draw.
        
        Returns:
            bool: True if the game is a draw, False otherwise
            
        Note:
            A draw occurs when all cells are filled and no player has won.
        """
        return all(self.board[r][c] for r in range(3) for c in range(3)) and not self.winner

    def to_dict(self):
        """
        Convert the game state to a dictionary for serialization.
        
        Returns:
            dict: Dictionary containing board, current player, and winner information
        """
        return {'board': self.board, 'current': self.current, 'winner': self.winner}

    @classmethod
    def from_dict(cls, d):
        """
        Create a TicTacToe instance from a dictionary.
        
        Args:
            d (dict): Dictionary containing board, current, and winner keys
            
        Returns:
            TicTacToe: New TicTacToe instance with the state from the dictionary
        """
        return cls(d['board'], d['current'], d['winner'])