from tests_example.app.sous_chef import SousChef
from tests_example.app.i_cooking_artifact import ICookingArtifact

class FakeArtifact(ICookingArtifact):
    def cook(self, minutes: int) -> str:
        return f"Cooked for {minutes} minutes"

    def get_cooking_state(self) -> str:
        return "raw"

def test_sous_chef_zero_ingredients():
    # Configuration
    artifact = FakeArtifact()
    sous_chef = SousChef([artifact])

    # Execution and verification
    assert sous_chef.adjust_cooking_time(10, 0) == ["Cooked for 10.0 minutes"]