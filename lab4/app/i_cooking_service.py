from abc import ABC, abstractmethod
from tests_example.app.models.recipe import Recipe

class ICookingService(ABC):
    @abstractmethod
    def cook_recipe(self, recipe:Recipe, minutes: int) -> str:
        pass

    @abstractmethod
    def get_cooking_state(self) -> str:
        pass
