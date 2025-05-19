from tests_example.app.slow_cooking_service import SlowCookingService
from tests_example.app.models.recipe import Recipe
from unittest.mock import MagicMock, patch
import time

def test_slow_cooking_service_initialization():
    service = SlowCookingService()
    assert service is not None

def test_slow_cooking_service_state():
    service = SlowCookingService()
    assert service.get_cooking_state() == "Cooking"

def test_slow_cooking_service_cook_recipe():
    service = SlowCookingService()
    mock_recipe = MagicMock()
    
    # Test with a short time to avoid long waits
    result = service.cook_recipe(mock_recipe, 0.1)
    assert result == "Done"

def test_slow_cooking_service_with_real_recipe():
    service = SlowCookingService()
    mock_artifact = MagicMock()
    recipe = Recipe([mock_artifact])
    
    # Test with a short time to avoid long waits
    result = service.cook_recipe(recipe, 0.1)
    assert result == "Done"

def test_slow_cooking_service_time_elapsed():
    service = SlowCookingService()
    mock_recipe = MagicMock()
    
    start_time = time.time()
    service.cook_recipe(mock_recipe, 0.1)
    end_time = time.time()
    
    # Verify that at least 0.1 seconds have passed
    assert end_time - start_time >= 0.1 