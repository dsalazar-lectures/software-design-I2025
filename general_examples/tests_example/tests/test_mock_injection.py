from tests_example.app.models.recipe import Recipe
from tests_example.app.oven_cooking_artifact import OvenArtifact
from tests_example.app.salt_cooking_seasoning import SaltSeasoning
from tests_example.tests.mocked_models.mock_cooking_service import MockCookingService

def test_recipe_with_mock_service():
    oven = OvenArtifact()
    salt = SaltSeasoning(20);
    recipe = Recipe([oven], [salt])
    mock_service = MockCookingService(recipe)

    result = mock_service.cook_recipe(12)
    assert recipe.get_all_states() == ["new"]
    assert recipe.get_all_seasonings_states() == ["not added"]
    assert "Mock cooked for 12 min" == result
