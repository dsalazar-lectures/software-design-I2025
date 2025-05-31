from tests_example.app.models.recipe import Recipe
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

def test_add_all_seasonings():
    mock_artifact1 = MagicMock()  # Solo para poder crear la receta
    mock_seasoning1 = MagicMock()

    mock_seasoning1.add.return_value = "added"
    
    recipe = Recipe([mock_artifact1], [mock_seasoning1])

    results = recipe.add_all_seasonings()

    assert results == ["added"]
    mock_seasoning1.add.assert_called_once()

def test_get_all_seasonings_states():
    mock_artifact1 = MagicMock()  # Solo para poder crear la receta
    mock_seasoning1 = MagicMock()
    mock_seasoning2 = MagicMock()

    mock_seasoning1.get_seasonig_state.return_value = "not added"
    mock_seasoning2.get_seasonig_state.return_value = "added"

    recipe = Recipe([mock_artifact1], [mock_seasoning1, mock_seasoning2])

    states = recipe.get_all_seasonings_states()

    assert states == ["not added", "added"]
    mock_seasoning1.get_seasonig_state.assert_called_once()
    mock_seasoning2.get_seasonig_state.assert_called_once()