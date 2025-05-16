from lab4.app.models.recipe import Recipe
from lab4.tests.mocked_models.dummy_artifact import DummyArtifact

def test_recipe_with_dummy_artifact():
    dummy = DummyArtifact()
    recipe = Recipe([dummy])
    result = recipe.cook_all(5)
    assert result[0] == "Dummy cooked for 5"
    assert recipe.get_all_states() == ["done"]
