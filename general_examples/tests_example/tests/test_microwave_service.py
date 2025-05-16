from tests_example.app.microwave_cooking_artifact import MicrowaveArtifact
from tests_example.app.models.recipe import Recipe
from tests_example.app.i_microwave_cooking_service import MicrowaveCookingService

def test_microwave_service_cooked_successfully():
    microwave = MicrowaveArtifact()
    recipe = Recipe([microwave])
    service = MicrowaveCookingService(recipe)

    result = service.cook_recipe(recipe, 10)
    assert result == "MicrowaveCookingService cooked recipe for 10 minutes"
    assert service.get_cooking_state() == "cooked"

def test_microwave_service_returns_warning_state():
    microwave = MicrowaveArtifact()
    recipe = Recipe([microwave])
    service = MicrowaveCookingService(recipe)

    result = service.cook_recipe(recipe, 2)
    assert result == "MicrowaveCookingService cooked recipe for 2 minutes"
    assert service.get_cooking_state() == "warming"

def test_microwave_service_handles_error_state():
    microwave = MicrowaveArtifact()
    recipe = Recipe([microwave])
    service = MicrowaveCookingService(recipe)

    result = service.cook_recipe(recipe, 70)
    assert result == "MicrowaveCookingService failed: at least one artifact returned an error"
    assert service.get_cooking_state() == "error"