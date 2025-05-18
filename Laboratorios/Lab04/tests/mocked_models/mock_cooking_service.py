from Lab04.app.i_cooking_service import ICookingService
from Lab04.app.i_cooking_artifact import ICookingArtifact
from typing import List
from Lab04.app.models.recipe import Recipe

class MockCookingService(ICookingService):
    def __init__(self, recipe: Recipe):
        self.last_minutes = 0
        self.state = "raw"
        self.recipe = recipe

    def cook_recipe(self, minutes: int) -> str:
        self.last_minutes = minutes
        self.state = "cooked" if minutes >= 10 else "undercooked"
        return f"Mock cooked for {minutes} min"

    def get_cooking_state(self) -> str:
        return self.state
