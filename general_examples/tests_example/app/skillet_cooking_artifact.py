from .i_cooking_artifact import ICookingArtifact

class SkilletArtifact(ICookingArtifact):
    def __init__(self):
        print("SkilletArtifact initialized")
        self.state = "raw"

    def cook(self, minutes: int) -> str:
        if minutes <= 0:
            self.state = "still raw"
        elif minutes < 2:
            self.state = "blue"  
        elif minutes < 4:
            self.state = "red"  
        elif minutes < 6:
            self.state = "medium red"  
        elif minutes < 8:
            self.state = "medium"  
        elif minutes < 10:
            self.state = "medium well"  
        elif minutes < 15:
            self.state = "well done"  
        else:
            self.state = "burnt"      
        return f"Cooked for {minutes} min, your meat is {self.state}."

    def get_cooking_state(self) -> str:
        print("Getting cooking state from the skillet.")
        return self.state
