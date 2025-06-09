from tests_example.app.models.recipe import Recipe
from tests_example.app.i_cooking_service import ICookingService
from tests_example.app.termometer_artifact import Termometer_Artifact

class Termometer_Service(ICookingService):
    def __init__(self, artifact : Termometer_Artifact):
         self.artifact = artifact
    
    def cook_recipe(self, recipe: Recipe, minutes: int)->str:
         doness = self.artifact.cook(minutes)
        
         return doness
    
    def get_cooking_state(self)->str:
         return self.artifact.get_cooking_state()