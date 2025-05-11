from tests_example.app.i_cooking_artifact import ICookingArtifact

class SlowCookerArtifact(ICookingArtifact):
    def __init__(self):
        print("SlowCookerArtifact initialized")
        self.state = "raw"

    def cook(self, minutes: int) -> str:
        print(f"Slow cooking for {minutes} minutes.")
        self.state = "cooked"
        return f"Slow cooked for {minutes} min"

    def get_cooking_state(self) -> str:
        print("Checking slow cooker state.")
        return self.state