from ..app.models.recipe import Recipe
from ..app.meat_cooking_service import MeatCookingService
from ..app.skillet_cooking_artifact import SkilletArtifact

def test_cook_recipe_blue():
    skillet = SkilletArtifact()
    recipe = Recipe([skillet])
    service = MeatCookingService(recipe)
    result = service.cook_recipe(7)
    state = service.get_cooking_state()
    assert result[0] == "Cooked for 7 min, your meat is medium."
    assert state[0] == "medium"

def test_cook_recipe_burnt():
    skillet = SkilletArtifact()
    recipe = Recipe([skillet])
    service = MeatCookingService(recipe)
    result = service.cook_recipe(20)
    state = service.get_cooking_state()
    assert result[0] == "Cooked for 20 min, your meat is burnt."
    assert state[0] == "burnt"

def test_cook_recipe_raw():
    skillet = SkilletArtifact()
    recipe = Recipe([skillet])
    service = MeatCookingService(recipe)
    result = service.cook_recipe(0)
    state = service.get_cooking_state()
    assert result[0] == "Cooked for 0 min, your meat is still raw."
    assert state[0] == "still raw"