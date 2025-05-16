from tests_example.app.i_cooking_service import ICookingService
from tests_example.app.models.recipe import Recipe
from tests_example.app.smart_microwave_artifact import SmartMicrowaveArtifact

class SmartMicrowaveService(ICookingService):
    def __init__(self, recipe: Recipe):
        self.recipe = recipe
        self.last_state = "raw"

    def cook_recipe(self, recipe: Recipe, minutes: int) -> str:
        self.recipe = recipe
        results = []
        for artifact in recipe.artifacts:
            result = artifact.cook(minutes)
            results.append(result)
        self.last_state = self.get_cooking_state()
        return "; ".join(results)

    def get_cooking_state(self) -> str:
        states = self.recipe.get_all_states()
        if all(state == "perfect" for state in states):
            return "perfect"
        elif any(state == "overcooked" for state in states):
            return "some overcooked"
        elif any(state == "undercooked" for state in states):
            return "some undercooked"
        else:
            return "mixed"
