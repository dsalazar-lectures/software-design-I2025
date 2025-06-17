from Lab04.app.models.recipe import Recipe
from Lab04.app.oven_cooking_artifact import OvenArtifact
from Lab04.tests.mocked_models.mock_cooking_service import MockCookingService

def test_recipe_with_mock_service():
    oven = OvenArtifact()
    recipe = Recipe([oven])
    mock_service = MockCookingService(recipe)

    result = mock_service.cook_recipe(12)
    assert recipe.get_all_states() == ["new"]
    assert "Mock cooked for 12 min" == result
