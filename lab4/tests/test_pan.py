from lab4.app.models.recipe import Recipe
from lab4.app.pan_artifact import PanArtifact

def test_oil_greasing():
    pan = PanArtifact()
    pan.grease("oil")
    assert pan.state == "greased"

def test_animal_fat_greasing():
    pan = PanArtifact()
    pan.grease("animal fat")
    assert pan.state == "greased"

def test_butter_greasing():
    pan = PanArtifact()
    pan.grease("butter")
    assert pan.state == "greased"

def test_failed_greasing():
    pan = PanArtifact()
    pan.grease("sugar")
    assert pan.state != "greased"

def test_pan_cooking_with_grease():
    pan = PanArtifact()
    pan.grease("oil")
    pan.cook(10)
    assert pan.state == "cooked"

def test_pan_cooking_without_grease():
    pan = PanArtifact()
    pan.cook(10)
    assert pan.state != "cooked"
