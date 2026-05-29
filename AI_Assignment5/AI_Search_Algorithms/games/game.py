from abc import ABC, abstractmethod


class GameState(ABC):

    @abstractmethod
    def get_legal_moves(self):
        pass

    @abstractmethod
    def make_move(self, move):
        pass

    @abstractmethod
    def is_terminal(self):
        pass

    @abstractmethod
    def evaluate(self):
        pass

    @abstractmethod
    def current_player(self):
        pass