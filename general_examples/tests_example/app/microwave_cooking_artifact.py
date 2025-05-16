from tests_example.app.i_cooking_artifact import ICookingArtifact

class MicrowaveArtifact(ICookingArtifact):
    def __init__(self):
        print("MicrowaveArtifact initialized")
        self.state = "new"

    def cook(self, minutes):
        print(f"Cooking for {minutes} minutes in the microwave.")
        self.state = "cooked"

    def get_cooking_state(self):
        print("Getting cooking state from the microwave.")
        return self.state