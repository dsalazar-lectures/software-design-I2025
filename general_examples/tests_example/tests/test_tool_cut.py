from tests_example.app.models.kitchener import Kitchener
from tests_example.app.knife_cut_tool import KnifeCutTool
from tests_example.app.oven_cooking_artifact import OvenArtifact

def test_kitchener_cut_tool():
    # Create instances of the tool and artifact
    knife_tool = KnifeCutTool()
    oven = OvenArtifact()

    # Create an instance of Kitchener with the tool and artifact
    kitchener = Kitchener(knife_tool, oven)

    # Test cutting food
    cut_result = kitchener.cut_food(5)
    assert cut_result == "Cutting for 5 minutes with the knife."

def test_kitchener_cook_food():
    # Create instances of the tool and artifact
    knife_tool = KnifeCutTool()
    oven = OvenArtifact()

    # Create an instance of Kitchener with the tool and artifact
    kitchener = Kitchener(knife_tool, oven)

    # Test cooking food
    cook_result = kitchener.cook_food(10)
    assert cook_result == "Cooking for 10 minutes in the oven."

def test_kitchener_cut_and_cook_food():
    # Create instances of the tool and artifact
    knife_tool = KnifeCutTool()
    oven = OvenArtifact()

    # Create an instance of Kitchener with the tool and artifact
    kitchener = Kitchener(knife_tool, oven)

    # Test cutting and then cooking food
    cut_result = kitchener.cut_food(3)
    cook_result = kitchener.cook_food(7)

    assert cut_result == "Cutting for 3 minutes with the knife."
    assert cook_result == "Cooking for 7 minutes in the oven."




