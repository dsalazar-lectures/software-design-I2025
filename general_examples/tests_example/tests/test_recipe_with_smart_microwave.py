from tests_example.app.smart_microwave_artifact import SmartMicrowaveArtifact
from tests_example.app.smart_microwave_service import SmartMicrowaveService
from tests_example.app.models.recipe import Recipe

def test_service_cooks_recipe_perfect():
    microwave = SmartMicrowaveArtifact()
    recipe = Recipe([microwave])
    service = SmartMicrowaveService(recipe)

    result = service.cook_recipe(recipe, 5)
    assert result == "Microwave cooked for 5 minutes."
    assert service.get_cooking_state() == "perfect"

def test_service_cooks_mixed_states():
    microwave1 = SmartMicrowaveArtifact()
    microwave2 = SmartMicrowaveArtifact()
    recipe = Recipe([microwave1, microwave2])
    service = SmartMicrowaveService(recipe)

    microwave1.cook(2)  # undercooked
    microwave2.cook(8)  # overcooked

    assert service.get_cooking_state() == "some overcooked"
