from tests_example.app.microwave_cooking_artifact import MicrowaveArtifact
from unittest.mock import patch

def test_microwave_initialization():
    microwave = MicrowaveArtifact()
    assert microwave.state == "new"

def test_microwave_cooking():
    microwave = MicrowaveArtifact()
    microwave.cook(5)
    assert microwave.state == "cooked"

def test_microwave_cooking_state():
    microwave = MicrowaveArtifact()
    assert microwave.get_cooking_state() == "new"
    microwave.cook(5)
    assert microwave.get_cooking_state() == "cooked"

def test_microwave_cooking_with_print():
    microwave = MicrowaveArtifact()
    with patch('builtins.print') as mock_print:
        microwave.cook(5)
        mock_print.assert_called_with("Cooking for 5 minutes in the microwave.") 