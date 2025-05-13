from typing import List
from tests_example.app.i_cooking_artifact import ICookingArtifact

class SousChef:
    def __init__(self, artifacts: List[ICookingArtifact]):
        self.artifacts = artifacts

    def adjust_cooking_time(self, base_minutes: int, ingredient_count: int) -> List[str]:
        adjusted_minutes = base_minutes * (1 + ingredient_count / 10)
        return [artifact.cook(adjusted_minutes) for artifact in self.artifacts]