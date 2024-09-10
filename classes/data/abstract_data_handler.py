from abc import ABC, abstractmethod

class AbstractDataHandler(ABC):
    
    @abstractmethod
    def save(self, *args, **kargs):
        pass

    @abstractmethod
    def find(self, id):
        pass
