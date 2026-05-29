import random
import math


class Node:

    def __init__(self, state, parent=None):

        self.state = state
        self.parent = parent

        self.children = []
        self.visits = 0
        self.wins = 0

    def fully_expanded(self):

        return len(self.children) == len(
            self.state.get_legal_moves()
        )

    def best_child(self, c=1.41):

        return max(
            self.children,
            key=lambda child:
            child.wins / (child.visits + 1e-9)
            + c * math.sqrt(
                math.log(self.visits + 1)
                / (child.visits + 1e-9)
            )
        )


def rollout(state):

    current = state

    while not current.is_terminal():

        move = random.choice(
            current.get_legal_moves()
        )

        current = current.make_move(move)

    return current.evaluate()


def mcts(root_state, iterations=1000):

    root = Node(root_state)

    for _ in range(iterations):

        node = root

        while node.children and node.fully_expanded():
            node = node.best_child()

        if not node.state.is_terminal():

            tried = [
                child.state.board
                for child in node.children
            ]

            for move in node.state.get_legal_moves():

                new_state = node.state.make_move(move)

                if new_state.board not in tried:

                    child = Node(new_state, node)
                    node.children.append(child)

                    node = child
                    break

        result = rollout(node.state)

        while node:

            node.visits += 1

            if result == 1:
                node.wins += 1

            node = node.parent

    best = max(
        root.children,
        key=lambda n: n.visits
    )

    return best.state