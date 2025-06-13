class TicTacToe:
    def __init__(self, board=None, current='X', winner=None):
        self.board = board if board else [['' for _ in range(3)] for _ in range(3)]
        self.current = current
        self.winner = winner

    def make_move(self, row, col):
        if self.board[row][col] or self.winner:
            return False
        self.board[row][col] = self.current
        if self.check_win(self.current):
            self.winner = self.current
        elif self.is_draw():
            self.winner = 'Draw'
        else:
            self.current = 'O' if self.current == 'X' else 'X'
        return True

    def check_win(self, player):
        b = self.board
        for i in range(3):
            if all(b[i][j] == player for j in range(3)):  # rows
                return True
            if all(b[j][i] == player for j in range(3)):  # cols
                return True
        if all(b[i][i] == player for i in range(3)):      # main diag
            return True
        if all(b[i][2-i] == player for i in range(3)):    # anti diag
            return True
        return False

    def is_draw(self):
        return all(self.board[r][c] for r in range(3) for c in range(3)) and not self.winner

    def to_dict(self):
        return {'board': self.board, 'current': self.current, 'winner': self.winner}

    @classmethod
    def from_dict(cls, d):
        return cls(d['board'], d['current'], d['winner'])