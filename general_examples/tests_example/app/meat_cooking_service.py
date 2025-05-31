from tests_example.app.i_cooking_service import ICookingService
from tests_example.app.models.recipe import Recipe

class MeatCookingService(ICookingService):
    """
    Service class for cooking meat recipes, implementing the ICookingService interface.
    Attributes:
        recipe (Recipe): The recipe associated with this cooking service.
    Methods:
        cook_recipe(recipe: Recipe, minutes: int) -> str:
            Cooks the given recipe for the specified minutes and updates the cooking state.
        get_cooking_state() -> str:
            Returns the current cooking state of the meat.
    """
    def __init__(self, recipe: Recipe):
        self.recipe = recipe

    def cook_recipe(self, minutes: int) -> str:
        return self.recipe.cook_all(minutes);

    def get_cooking_state(self) -> str:
        return self.recipe.get_all_states()