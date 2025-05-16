from tests_example.app.i_cooking_service import ICookingService
from tests_example.app.models.recipe import Recipe

class AdvancedCookingService(ICookingService):
    def __init__(self,recipe:Recipe):
        self.recipe = recipe
        self.state = "not started"

    def cook_recipe(self, minutes: int)-> str:
        results = self.recipe.cook_all(minutes)
        if any("failed" in r for r in results):
            self.state = "error"
            return "Cooking halted: one or more artifacts failed"
        self.state = "done"
        return "All artifacts cooked successfully"
    
    def get_cooking_state(self) -> str:
        return self.state