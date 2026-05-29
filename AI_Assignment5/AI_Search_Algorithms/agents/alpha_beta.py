def alpha_beta(state, alpha, beta, maximizing):

    if state.is_terminal():
        return state.evaluate(), None

    best_move = None

    if maximizing:

        value = float('-inf')

        for move in state.get_legal_moves():

            score, _ = alpha_beta(
                state.make_move(move),
                alpha,
                beta,
                False
            )

            if score > value:
                value = score
                best_move = move

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value, best_move

    else:

        value = float('inf')

        for move in state.get_legal_moves():

            score, _ = alpha_beta(
                state.make_move(move),
                alpha,
                beta,
                True
            )

            if score < value:
                value = score
                best_move = move

            beta = min(beta, value)

            if alpha >= beta:
                break

        return value, best_move