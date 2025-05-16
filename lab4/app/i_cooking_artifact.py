from abc import ABC, abstractmethod

class ICookingArtifact(ABC):
    @abstractmethod
    def cook(self, minutes: int) -> str:
        """Cocina por una cantidad de minutos."""
        pass

    @abstractmethod
    def get_cooking_state(self) -> str:
        """Consulta el estado de cocción."""
        pass