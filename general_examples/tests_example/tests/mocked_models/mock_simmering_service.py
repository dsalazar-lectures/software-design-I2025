from tests_example.app.i_simmering_service import ISimmeringService
from tests_example.app.i_simmering_capable_artifact import ISimmeringCapableArtifact
from tests_example.app.i_cooking_artifact import ICookingArtifact
from tests_example.app.pot_cooking_artifact import PotArtifact
from typing import List

class MockSimmeringService(ISimmeringService):
    def __init__(self, pot: ICookingArtifact):
        self.last_minutes = 0
        self.state = "raw"
        self.pot = pot

    def cook_recipe(self, minutes: int) -> str:
        self.last_minutes = minutes
        self.state = "cooked" if minutes >= 10 else "undercooked"
        return f"Mock cooked for {minutes} min"

    def get_cooking_state(self) -> str:
        return self.state

    def simmering(self, minutes: int):
        if not isinstance(self.pot, ISimmeringCapableArtifact):
            #raise ValueError("Este artefacto no permite cocción a fuego lento.")
            result = "ValueError: Este artefacto no permite cocción a fuego lento"
        else:
            result = self.pot.simmer(minutes)
            self.state = self.pot.get_cooking_state()
        return result
        
