from abc import ABC, abstractmethod

class AbstractGame(ABC):
    @abstractmethod
    def add_game(self):
        pass

    @abstractmethod
    def replace_game(index, value):
        pass

    @abstractmethod
    def reset_games():
        pass
