from Lab04.app.models.recipe import Recipe
from unittest.mock import MagicMock

def test_cook_all():
    mock_artifact1 = MagicMock()
    mock_artifact2 = MagicMock()

    mock_artifact1.cook.return_value = "Done in air fryer"
    mock_artifact2.cook.return_value = "Done in oven"

    recipe = Recipe([mock_artifact1, mock_artifact2])

    results = recipe.cook_all(10)

    assert results == ["Done in air fryer", "Done in oven"]
    mock_artifact1.cook.assert_called_once_with(10)
    mock_artifact2.cook.assert_called_once_with(10)

def test_get_all_states():
    mock_artifact1 = MagicMock()
    mock_artifact2 = MagicMock()

    mock_artifact1.get_cooking_state.return_value = "Ready"
    mock_artifact2.get_cooking_state.return_value = "Still cooking"

    recipe = Recipe([mock_artifact1, mock_artifact2])

    states = recipe.get_all_states()

    assert states == ["Ready", "Still cooking"]
    mock_artifact1.get_cooking_state.assert_called_once()
    mock_artifact2.get_cooking_state.assert_called_once()
