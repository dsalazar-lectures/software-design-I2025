from tests_example.app.i_cooking_artifact import ICookingArtifact

class MicrowaveArtifact(ICookingArtifact):
    def __init__(self):
        print("MicrowaveArtifact initialized")
        self.state = "new"

    def cook(self, minutes):
        if minutes > 60:
            self.state = "error"
            return "Error: too long for microwave"
        elif minutes < 3:
            self.state = "warming"
        else:
            self.state = "cooked"
        print(f"Cooking for {minutes} minutes in the microwave.")
        return f"Microwave cooked for {minutes}"

    def get_cooking_state(self):
        print("Getting cooking state from the microwave.")
        return self.state