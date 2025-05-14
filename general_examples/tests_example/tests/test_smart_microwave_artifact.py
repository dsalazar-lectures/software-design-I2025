from tests_example.app.smart_microwave_artifact import SmartMicrowaveArtifact

def test_microwave_cooks_undercooked():
    microwave = SmartMicrowaveArtifact()
    result = microwave.cook(2)
    assert result == "Microwave cooked for 2 minutes."
    assert microwave.get_cooking_state() == "undercooked"

def test_microwave_cooks_perfect():
    microwave = SmartMicrowaveArtifact()
    result = microwave.cook(5)
    assert result == "Microwave cooked for 5 minutes."
    assert microwave.get_cooking_state() == "perfect"

def test_microwave_cooks_overcooked():
    microwave = SmartMicrowaveArtifact()
    result = microwave.cook(9)
    assert result == "Microwave cooked for 9 minutes."
    assert microwave.get_cooking_state() == "overcooked"
