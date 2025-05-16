from tests_example.app.microwave_cooking_artifact import MicrowaveArtifact

def test_microwave_cook_under_3_minutes():
    mw = MicrowaveArtifact()
    result = mw.cook(2)
    assert result == "Microwave cooked for 2"
    assert mw.get_cooking_state() == "warming"

def test_microwave_cook_normal():
    mw = MicrowaveArtifact()
    result = mw.cook(10)
    assert result == "Microwave cooked for 10"
    assert mw.get_cooking_state() == "cooked"

def test_microwave_cook_too_long():
    mw = MicrowaveArtifact()
    result = mw.cook(70)
    assert result == "Error: too long for microwave"
    assert mw.get_cooking_state() == "error"