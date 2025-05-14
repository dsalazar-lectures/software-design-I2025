from abc import ABC, abstractmethod

class ICookingArtifact(ABC):
    temperature: int

    @abstractmethod
    def cook(self, minutes: int) -> str:
        """Cocina por una cantidad de minutos."""
        pass

    @abstractmethod
    def get_cooking_state(self) -> str:
        """Consulta el estado de cocción."""
        pass

    @abstractmethod
    def set_cooking_temperature(self):
        """Establece la temperatura de cocción."""
        pass