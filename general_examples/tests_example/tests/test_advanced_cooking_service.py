from tests_example.app.models.recipe import Recipe
from tests_example.app.oven_cooking_artifact import OvenArtifact
from tests_example.app.smart_oven_artifact import SmartOvenArtifact
from tests_example.app.advanced_cooking_service import AdvancedCookingService

def test_advanced_service_success():
    smart = SmartOvenArtifact()
    oven = OvenArtifact()
    recipe = Recipe([smart,oven])
    service = AdvancedCookingService(recipe)

    result = service.cook_recipe(10)

    assert result == "All artifacts cooked successfully"
    assert service.get_cooking_state() == "done"



def test_advanced_service_failure():
    smart = SmartOvenArtifact()
    oven = OvenArtifact()
    recipe = Recipe([smart,oven])
    service = AdvancedCookingService(recipe)

    result = service.cook_recipe(3)

    assert result == "Cooking halted: one or more artifacts failed"
    assert service.get_cooking_state() == "error"
