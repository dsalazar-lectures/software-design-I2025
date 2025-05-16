from tests_example.app.i_cooking_artifact import ICookingArtifact

class OvenArtifact(ICookingArtifact):
    def __init__(self):
        print("OvenArtifact initialized")
        self.state = "new"

    def cook(self, minutes):
        print(f"Cooking for {minutes} minutes in the oven.")
        self.state = "cooked"
        return f"Oven cooked for {minutes} min"

    def get_cooking_state(self):
        print("Getting cooking state from the oven.")
        return self.state
