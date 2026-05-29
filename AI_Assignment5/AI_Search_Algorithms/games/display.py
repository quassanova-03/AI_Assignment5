def print_reference_board():

    print("=" * 50)
    print("      TIC-TAC-TOE POSITION REFERENCE")
    print("=" * 50)

    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")

    print()


def print_board_with_move(move):

    board = [str(i + 1) for i in range(9)]

    board[move] = "X"

    print()

    for row in range(3):

        start = row * 3

        print(
            f" {board[start]} | {board[start+1]} | {board[start+2]} "
        )

        if row != 2:
            print("-----------")

    print()