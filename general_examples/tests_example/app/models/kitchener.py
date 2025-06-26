from tests_example.app.i_tool_cut import IToolCut
from tests_example.app.i_cooking_artifact import ICookingArtifact

class Kitchener:
    def __init__(self, ToolCut: IToolCut, Artifact: ICookingArtifact):
        self.ToolCut = ToolCut
        self.Artifact = Artifact

    def cut_food(self, minutes: int) -> str:
        return self.ToolCut.cut(minutes)

    def cook_food(self, minutes: int) -> str:
        return self.Artifact.cook(minutes)
