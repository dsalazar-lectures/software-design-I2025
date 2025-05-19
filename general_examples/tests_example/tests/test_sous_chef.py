from tests_example.app.sous_chef import SousChef
from tests_example.app.i_cooking_artifact import ICookingArtifact

class FakeArtifact(ICookingArtifact):
    def cook(self, minutes: int) -> str:
        return f"Cooked for {minutes} minutes"

    def get_cooking_state(self) -> str:
        return "raw"

def test_sous_chef_adjusts_time():
    # Configuration
    fake_artifact = FakeArtifact()
    sous_chef = SousChef([fake_artifact])

    # Execution and verification
    assert sous_chef.adjust_cooking_time(10, 1) == ["Cooked for 11.0 minutes"]