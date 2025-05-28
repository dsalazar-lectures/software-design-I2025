from tests_example.app.smart_oven_artifact import SmartOvenArtifact

def test_successful_cooking():
    smart_oven = SmartOvenArtifact()
    result = smart_oven.cook(12)
    assert result == "Smart oven cooked at 192°C for 12 min"
    assert smart_oven.get_cooking_state()== "perfectly cooked"

def test_failed_cooking_short_time():
    smart_oven = SmartOvenArtifact()
    result = smart_oven.cook(3)
    assert result == "Cooking failed: time too short"
    assert smart_oven.get_cooking_state()== "undercooked"
