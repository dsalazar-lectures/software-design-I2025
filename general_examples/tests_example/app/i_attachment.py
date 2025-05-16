from abc import ABC, abstractmethod

class IAttachment(ABC):
    @abstractmethod
    def use(self, minutes: int) -> str:
        pass

    @abstractmethod
    def get_state(self) -> str:
        pass
