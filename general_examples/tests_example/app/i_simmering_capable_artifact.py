from abc import ABC, abstractmethod
from tests_example.app.i_cooking_artifact import ICookingArtifact

class ISimmeringCapableArtifact(ICookingArtifact):
    @abstractmethod
    def simmer(self, minutes: int) -> str:
        """Cocina a tiempo lento por una cantidad de minutos."""
        pass

