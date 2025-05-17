import time
from tests_example.app.i_cooking_service import ICookingService

class SlowCookingService(ICookingService):
    def cook_recipe(self, recipe, minutes):
        time.sleep(minutes)
        return "Done"

    def get_cooking_state(self):
        return "Cooking"