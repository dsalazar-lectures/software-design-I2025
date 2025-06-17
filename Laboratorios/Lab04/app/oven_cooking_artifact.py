from Lab04.app.i_cooking_artifact import ICookingArtifact

class OvenArtifact(ICookingArtifact):
    def __init__(self):
        print("OvenArtifact initialized")
        self.state = "new"

    def preheat(self, temperature):
        print(f"Preheating oven to {temperature}°C.")
        self.state = "preheated"

    def cook(self, minutes):
        print(f"Cooking for {minutes} minutes in the oven.")
        self.state = "cooked"

    def get_cooking_state(self):
        print("Getting cooking state from the oven.")
        return self.state
