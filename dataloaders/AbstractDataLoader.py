from abc import ABC, abstractmethod

class AbstractDataLoader(ABC):
    def __init__(self) -> None:
        self.label_type

    @abstractmethod
    def get(self,id):
        return True

        