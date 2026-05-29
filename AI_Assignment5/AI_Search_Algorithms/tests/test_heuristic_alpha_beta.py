from games.tic_tac_toe import TicTacToe
from agents.heuristic_alpha_beta import heuristic_alpha_beta


def test_heuristic():

    state = TicTacToe()

    score, move = heuristic_alpha_beta(
        state,
        3,
        float('-inf'),
        float('inf'),
        True
    )

    assert move is not None