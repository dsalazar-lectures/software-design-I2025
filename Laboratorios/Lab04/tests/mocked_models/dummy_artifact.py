from Lab04.app.i_cooking_artifact import ICookingArtifact

class DummyArtifact(ICookingArtifact):
    def __init__(self):
        self.cooked = False

    def cook(self, minutes):
        self.cooked = True
        return f"Dummy cooked for {minutes}"

    def get_cooking_state(self):
        return "done" if self.cooked else "waiting"
