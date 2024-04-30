from abc import ABC, abstractmethod

class AbstractGame(ABC):
    
    @property
    @abstractmethod
    def URL(self, date) -> str:
        pass

    @abstractmethod
    def add_game(self):
        pass

    @abstractmethod
    def replace_game(index, value):
        pass

    @abstractmethod
    def reset_games():
        pass
