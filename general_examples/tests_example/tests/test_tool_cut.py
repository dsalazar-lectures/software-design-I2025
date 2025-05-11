
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

