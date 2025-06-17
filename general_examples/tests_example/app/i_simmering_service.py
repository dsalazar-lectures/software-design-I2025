from abc import ABC, abstractmethod
from tests_example.app.i_cooking_service import ICookingService
from tests_example.app.i_simmering_capable_artifact import ISimmeringCapableArtifact


class ISimmeringService(ICookingService):
    @abstractmethod
    def simmering(self, pot: ISimmeringCapableArtifact, minutes: int) -> str:
        pass
