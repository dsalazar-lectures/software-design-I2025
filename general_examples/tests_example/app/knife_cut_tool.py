from tests_example.app.i_tool_cut import IToolCut

class KnifeCutTool(IToolCut):
    def __init__(self):
        print("KnifeCutTool initialized")
    
    def cut(self, minutes):
        return f"Cutting for {minutes} minutes with the knife."
    
    def get_cutting_state(self):
        return f"Getting cutting state from the knife."