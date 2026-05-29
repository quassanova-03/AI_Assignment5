def minimax(state, maximizing):

    if state.is_terminal():
        return state.evaluate(), None

    best_move = None

    if maximizing:

        best_score = float('-inf')

        for move in state.get_legal_moves():

            score, _ = minimax(
                state.make_move(move),
                False
            )

            if score > best_score:
                best_score = score
                best_move = move

        return best_score, best_move

    else:

        best_score = float('inf')

        for move in state.get_legal_moves():

            score, _ = minimax(
                state.make_move(move),
                True
            )

            if score < best_score:
                best_score = score
                best_move = move

        return best_score, best_move