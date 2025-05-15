from unittest.mock import MagicMock
from tests_example.app.cooking_service import CookingService
from tests_example.app.models.recipe import Recipe

def test_cook_recipe_calls_artifact_correctly():
    mock_artifact = MagicMock()
    mock_artifact.cook.return_value = "Término simulado" #esto solo para efectos de laprueba marco jeje

    service = CookingService(mock_artifact)
    dummy_recipe = MagicMock(spec=Recipe)  

    result = service.cook_recipe(dummy_recipe, 5)

    mock_artifact.cook.assert_called_once_with(5)
    assert result == "Término simulado"

def test_get_cooking_state_delegates_to_artifact():
    mock_artifact = MagicMock()
    mock_artifact.get_cooking_state.return_value = "medium rare"

    service = CookingService(mock_artifact)

    assert service.get_cooking_state() == "medium rare"
    mock_artifact.get_cooking_state.assert_called_once()
