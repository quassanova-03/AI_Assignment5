from games.tic_tac_toe import TicTacToe
from games.display import (
    print_reference_board,
    print_board_with_move
)

from agents.minimax import minimax
from agents.alpha_beta import alpha_beta
from agents.heuristic_alpha_beta import heuristic_alpha_beta
from agents.mcts import mcts


def get_demo_state():
    """
    Board where X has an immediate winning move.

    Positions:

     X | X | 3
    -----------
     O | O | 6
    -----------
     7 | 8 | 9
    """

    board = [
        'X', 'X', ' ',
        'O', 'O', ' ',
        ' ', ' ', ' '
    ]

    return TicTacToe(board, 'X')


def run_minimax():

    state = get_demo_state()

    score, move = minimax(state, True)

    print("=" * 50)
    print("MINIMAX")
    print("=" * 50)

    print_board_with_move(move)

    print(f"Chosen Move = {move + 1}")
    print(f"Score = {score}")
    print()


def run_alpha_beta():

    state = get_demo_state()

    score, move = alpha_beta(
        state,
        float('-inf'),
        float('inf'),
        True
    )

    print("=" * 50)
    print("ALPHA-BETA")
    print("=" * 50)

    print_board_with_move(move)

    print(f"Chosen Move = {move + 1}")
    print(f"Score = {score}")
    print()


def run_heuristic_alpha_beta():

    state = get_demo_state()

    score, move = heuristic_alpha_beta(
        state,
        4,
        float('-inf'),
        float('inf'),
        True
    )

    print("=" * 50)
    print("HEURISTIC ALPHA-BETA")
    print("=" * 50)

    print_board_with_move(move)

    print(f"Chosen Move = {move + 1}")
    print(f"Score = {score}")
    print()


def run_mcts():

    state = get_demo_state()

    best_state = mcts(state, 1000)

    move = None

    for i in range(9):

        if state.board[i] != best_state.board[i]:
            move = i
            break

    print("=" * 50)
    print("MONTE CARLO TREE SEARCH")
    print("=" * 50)

    print_board_with_move(move)

    print(f"Chosen Move = {move + 1}")
    print()


if __name__ == "__main__":

    print_reference_board()

    print("TEST BOARD:")
    print()

    print(" X | X | 3 ")
    print("-----------")
    print(" O | O | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")

    print()
    print("X to move.")
    print("The correct move is Position 3 (winning move).")
    print()

    run_minimax()

    run_alpha_beta()

    run_heuristic_alpha_beta()

    run_mcts()