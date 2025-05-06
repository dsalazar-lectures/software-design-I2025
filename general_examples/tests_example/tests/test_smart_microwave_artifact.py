from tests_example.app.smart_microwave_artifact import SmartMicrowaveArtifact

def test_smart_microwave_states():
    microwave = SmartMicrowaveArtifact()

    # Test undercooked
    result = microwave.cook(2)
    assert result == "Microwave cooked for 2 minutes."
    assert microwave.get_cooking_state() == "undercooked"

    # Test perfect
    result = microwave.cook(5)
    assert result == "Microwave cooked for 5 minutes."
    assert microwave.get_cooking_state() == "perfect"

    # Test overcooked
    result = microwave.cook(10)
    assert result == "Microwave cooked for 10 minutes."
    assert microwave.get_cooking_state() == "overcooked"
