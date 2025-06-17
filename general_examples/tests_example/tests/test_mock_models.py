from tests_example.app.models.recipe import Recipe
from tests_example.tests.mocked_models.dummy_artifact import DummyArtifact
from tests_example.tests.mocked_models.dummy_seasoning import DummySeasoning

def test_recipe_with_dummy_artifact():
    dummy = DummyArtifact()
    recipe = Recipe([dummy])
    result = recipe.cook_all(5)
    assert result[0] == "Dummy cooked for 5"
    assert recipe.get_all_states() == ["done"]

def test_recipe_with_dummy_seasoning():
    dummy = DummyArtifact()  # Solo para poder crear la receta
    dummySeasoning = DummySeasoning(50)

    recipe = Recipe([dummy], [dummySeasoning])

    result = recipe.add_all_seasonings()
    
    assert result[0] == "added 50 grams of Dummy seasoning"
    assert recipe.get_all_seasonings_states() == ["added"]