from tests_example.app.i_cooking_service import ICookingService
from tests_example.app.models.recipe import Recipe

class MicrowaveCookingService(ICookingService):
    def __init__(self, recipe: Recipe):
        self.recipe = recipe
        self.last_minutes = 0
        self.last_states = []

    def cook_recipe(self, recipe: Recipe, minutes: int) -> str:
        self.last_minutes = minutes
        recipe.cook_all(minutes)
        self.last_states = recipe.get_all_states()

        if "error" in self.last_states:
            return "MicrowaveCookingService failed: at least one artifact returned an error"

        return f"MicrowaveCookingService cooked recipe for {minutes} minutes"

    def get_cooking_state(self) -> str:
        return ", ".join(self.last_states)