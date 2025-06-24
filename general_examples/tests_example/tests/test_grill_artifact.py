import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from tests_example.app.grill_cooking_artifact import GrillArtifact

def test_initial_state():
    grill = GrillArtifact()
    assert grill.get_cooking_state() == "raw"
    print("Test passed: Initial state")

def test_cook_rare():
    grill = GrillArtifact()
    result = grill.cook(3)
    assert grill.get_cooking_state() == "rare"
    assert result == "Grilled for 3 minutes."
    print("Test passed: Cook rare")

def test_cook_medium():
    grill = GrillArtifact()
    result = grill.cook(5)
    assert grill.get_cooking_state() == "medium"
    assert result == "Grilled for 5 minutes."
    print("Test passed: Cook medium")

def test_cook_medium_well():
    grill = GrillArtifact()
    result = grill.cook(7)
    assert grill.get_cooking_state() == "medium well"
    assert result == "Grilled for 7 minutes."
    print("Test passed: Cook medium well")

def test_cook_well_done():
    grill = GrillArtifact()
    result = grill.cook(10)
    assert grill.get_cooking_state() == "well done"
    assert result == "Grilled for 10 minutes."
    print("Test passed: Cook well done")

def test_cook_burnt():
    grill = GrillArtifact()
    result = grill.cook(15)
    assert grill.get_cooking_state() == "burnt"
    assert result == "Grilled for 15 minutes."
    print("Test passed: Cook burnt")

def test_cook_edge_cases():
    grill = GrillArtifact()

    grill.cook(4)
    assert grill.get_cooking_state() == "medium"
    print("Test passed: Edge case 4 minutes")

    grill.cook(6)
    assert grill.get_cooking_state() == "medium well"
    print("Test passed: Edge case 6 minutes")

    grill.cook(9)
    assert grill.get_cooking_state() == "well done"
    print("Test passed: Edge case 9 minutes")

    grill.cook(12)
    assert grill.get_cooking_state() == "burnt"
    print("Test passed: Edge case 12 minutes")

# Ejecutar todos los tests
if __name__ == "__main__":
    test_initial_state()
    test_cook_rare()
    test_cook_medium()
    test_cook_medium_well()
    test_cook_well_done()
    test_cook_burnt()
    test_cook_edge_cases()
    print("\nTodos los tests pasaron correctamente.")