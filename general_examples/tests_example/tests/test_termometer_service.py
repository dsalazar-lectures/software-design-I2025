from unittest.mock import MagicMock
from tests_example.app.i_cooking_service import ICookingService
from tests_example.app.models.recipe import Recipe
from tests_example.app.termometer_service import Termometer_Service

def test_cook_recipe_calls_artifact_correctly():
    mock_artifact = MagicMock()
    mock_artifact.cook.return_value = "Término simulado"
    
    service = Termometer_Service(mock_artifact)  
    dummy_recipe = MagicMock() # esta es culaquier objeto, me tengo que acordar de esto del magic mocc
    
    result = service.cook_recipe(dummy_recipe, 5)
    assert result == "Término simulado"
    mock_artifact.cook.assert_called_once_with(5)


def test_get_cooking_state_delegates_to_artifact():
    mock_artifact = MagicMock()
    mock_artifact.get_cooking_state.return_value = "medium rare"

    service =  Termometer_Service(mock_artifact)

    assert service.get_cooking_state() == "medium rare"
    mock_artifact.get_cooking_state.assert_called_once()
