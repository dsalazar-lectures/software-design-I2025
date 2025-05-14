import pytest
from ..app.oven_cooking_artifact import OvenArtifact

def test_oven_initial_state():
    oven = OvenArtifact()
    assert oven.get_cooking_state() == "new"

def test_oven_preheat_changes_state():
    oven = OvenArtifact()
    oven.preheat(180)
    assert oven.get_cooking_state() == "preheated"

def test_oven_cook_after_preheat():
    oven = OvenArtifact()
    oven.preheat(200)
    oven.cook(30)
    assert oven.get_cooking_state() == "cooked"

def test_oven_cook_without_preheat():
    oven = OvenArtifact()
    oven.cook(20)
    assert oven.get_cooking_state() == "cooked"