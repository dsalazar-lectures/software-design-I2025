import pytest
from tests_example.app.termometer_artifact import Termometer_Artifact

from tests_example.app.termometer_artifact import Termometer_Artifact

def test_cook_sets_correct_status():
    artifact = Termometer_Artifact()

    artifact.cook(1)
    assert artifact.get_cooking_state() == "rare"

    artifact.cook(3)
    assert artifact.get_cooking_state() == "medium rare"

    artifact.cook(5)
    assert artifact.get_cooking_state() == "medium"

    artifact.cook(6)
    assert artifact.get_cooking_state() == "well done"
    
    artifact.cook(9)
    assert artifact.get_cooking_state() == "burned"