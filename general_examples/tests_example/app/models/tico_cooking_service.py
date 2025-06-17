from tests_example.app.i_cooking_service import ICookingService

class TicoCookingService(ICookingService):
    def __init__(self, artifact):
        self.artifact = artifact

    def cook_recipe(self, recipe, minutes: int) -> str:
        return recipe.cook_all(minutes)

    def get_cooking_state(self) -> str:
        return self.artifact.get_cooking_state()