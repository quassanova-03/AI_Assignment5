from games.game import GameState


class TicTacToe(GameState):

    def __init__(self, board=None, player='X'):
        self.board = board if board else [' '] * 9
        self.player = player

    def get_legal_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def make_move(self, move):
        new_board = self.board.copy()
        new_board[move] = self.player

        next_player = 'O' if self.player == 'X' else 'X'

        return TicTacToe(new_board, next_player)

    def current_player(self):
        return self.player

    def winner(self):

        lines = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]

        for a,b,c in lines:
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return self.board[a]

        return None

    def is_terminal(self):
        return self.winner() is not None or ' ' not in self.board

    def evaluate(self):

        w = self.winner()

        if w == 'X':
            return 1

        if w == 'O':
            return -1

        return 0

    def heuristic(self):
        """
        Simple evaluation for depth-limited search.
        """

        score = 0

        lines = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]

        for line in lines:

            vals = [self.board[i] for i in line]

            if vals.count('X') == 2 and vals.count(' ') == 1:
                score += 5

            if vals.count('O') == 2 and vals.count(' ') == 1:
                score -= 5

        return score