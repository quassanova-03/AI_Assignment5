def heuristic_alpha_beta(
        state,
        depth,
        alpha,
        beta,
        maximizing):

    if state.is_terminal():
        return state.evaluate(), None

    if depth == 0:
        return state.heuristic(), None

    best_move = None

    if maximizing:

        value = float('-inf')

        for move in state.get_legal_moves():

            score, _ = heuristic_alpha_beta(
                state.make_move(move),
                depth - 1,
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

            score, _ = heuristic_alpha_beta(
                state.make_move(move),
                depth - 1,
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