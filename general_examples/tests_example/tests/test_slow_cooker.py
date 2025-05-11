from tests_example.app.slow_cooker_artifact import SlowCookerArtifact
from tests_example.app.models.recipe import Recipe
from unittest.mock import MagicMock

def test_slow_cooker_cook():
    slow_cooker = SlowCookerArtifact()
    recipe = Recipe([slow_cooker])
    results = recipe.cook_all(120)
    assert results == ["Slow cooked for 120 min"]
    assert slow_cooker.get_cooking_state() == "cooked"

def test_slow_cooker_mock():
    mock_slow_cooker = MagicMock()
    mock_slow_cooker.cook.return_value = "Mocked slow cook"
    mock_slow_cooker.get_cooking_state.return_value = "simulated_cooked"
    
    recipe = Recipe([mock_slow_cooker])
    results = recipe.cook_all(90)
    
    assert results == ["Mocked slow cook"]
    mock_slow_cooker.cook.assert_called_once_with(90)
    mock_slow_cooker.get_cooking_state.assert_called_once()