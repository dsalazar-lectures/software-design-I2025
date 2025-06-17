from abc import ABC, abstractmethod

class IToolCut(ABC):
    @abstractmethod
    def cut(self, minutes: int) -> str:
        pass
    