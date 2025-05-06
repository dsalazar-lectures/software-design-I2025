from tests_example.app.models.recipe import Recipe
from tests_example.app.oven_cooking_artifact import OvenArtifact
from tests_example.tests.mocked_models.mock_cooking_service import MockCookingService

def test_recipe_with_mock_service():
    oven = OvenArtifact()
    recipe = Recipe([oven])
    mock_service = MockCookingService(recipe)

    result = mock_service.cook_recipe(12)
    assert recipe.get_all_states() == ["new"]
    assert "Mock cooked for 12 min" == result

def test_recipe_with_mock_service_undercooked():
    oven = OvenArtifact()
    recipe = Recipe([oven])
    mock_service = MockCookingService(recipe)

    result = mock_service.cook_recipe(5) # Not enough time to cook
    assert mock_service.get_cooking_state() == "undercooked"
    assert "Mock cooked for 5 min" == result

def test_recipe_with_mock_service_dropped():
    oven = OvenArtifact()
    recipe = Recipe([oven])
    mock_service = MockCookingService(recipe)

    result = mock_service.drop_cooking() # Drop the cooking
    assert mock_service.get_cooking_state() == "dropped"
    assert "Cooking dropped" == result