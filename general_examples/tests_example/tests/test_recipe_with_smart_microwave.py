from tests_example.app.smart_microwave_artifact import SmartMicrowaveArtifact
from tests_example.app.models.recipe import Recipe

def test_recipe_with_smart_microwave():
    microwave = SmartMicrowaveArtifact()
    recipe = Recipe([microwave])

    result = recipe.cook_all(6)
    assert result[0] == "Microwave cooked for 6 minutes."
    assert recipe.get_all_states() == ["perfect"]