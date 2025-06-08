from tests_example.app.i_cooking_artifact import ICookingArtifact

class SmartMicrowaveArtifact(ICookingArtifact):
    def __init__(self):
        self.state = "raw"

    def cook(self, minutes):
        print(f"Microwaving for {minutes} minutes.")
        if minutes < 3:
            self.state = "undercooked"
        elif 3 <= minutes <= 7:
            self.state = "perfect"
        else:
            self.state = "overcooked"
        return f"Microwave cooked for {minutes} minutes."

    def get_cooking_state(self):
        print("Getting cooking state from microwave.")
        return self.state
