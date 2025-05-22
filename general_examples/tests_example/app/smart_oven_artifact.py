from tests_example.app.i_cooking_artifact import ICookingArtifact

class SmartOvenArtifact(ICookingArtifact):
    def __init__(self):
        self.state = "ready"
        self.temperature = 0

    def cook(self, minutes:int) -> str:
        if minutes < 5:
            self.state = "undercooked"
            return "Cooking failed: time too short"
        self.temperature = 180 + minutes
        self.state = "perfectly cooked"
        return f"Smart oven cooked at {self.temperature}°C for {minutes} min"
    
    def get_cooking_state(self) -> str:
        return self.state