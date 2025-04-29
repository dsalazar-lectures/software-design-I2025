from tests_example.app.i_cooking_artifact import ICookingArtifact

class AirfryerArtifact(ICookingArtifact):
    def __init__(self):
        print("AirfryerArtifact initialized")

    def cook(self, minutes):
        print(f"Cooking for {minutes} minutes in the air fryer.")

    def get_cooking_state(self):
        print("Getting cooking state from the air fryer.")
