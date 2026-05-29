from games.tic_tac_toe import TicTacToe
from agents.mcts import mcts


def test_mcts():

    state = TicTacToe()

    result = mcts(state, 500)

    assert result is not None