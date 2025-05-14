from tests_example.app.i_cooking_artifact import ICookingArtifact

class OvenArtifact(ICookingArtifact):
    def __init__(self):
        self.temperature = 300
        print("OvenArtifact initialized")
        self.state = "new"

    def cook(self, minutes):
        print(f"Cooking for {minutes} minutes in the oven.")
        self.state = "cooked"

    def get_cooking_state(self):
        print("Getting cooking state from the oven.")
        return self.state
    
    def set_cooking_temperature(self, temperature):
        print(f"The temperature of the oven has been set to {temperature}°")
