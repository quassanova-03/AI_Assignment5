from games.tic_tac_toe import TicTacToe
from agents.alpha_beta import alpha_beta


def test_alpha_beta():

    board = [
        'X','X',' ',
        'O','O',' ',
        ' ',' ',' '
    ]

    state = TicTacToe(board,'X')

    score, move = alpha_beta(
        state,
        float('-inf'),
        float('inf'),
        True
    )

    assert move == 2