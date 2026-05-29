from games.tic_tac_toe import TicTacToe
from agents.minimax import minimax


def test_minimax_winning_move():

    board = [
        'X','X',' ',
        'O','O',' ',
        ' ',' ',' '
    ]

    state = TicTacToe(board,'X')

    score, move = minimax(state, True)

    assert move == 2