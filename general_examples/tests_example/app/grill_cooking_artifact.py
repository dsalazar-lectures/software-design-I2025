from tests_example.app.i_cooking_artifact import ICookingArtifact

class GrillArtifact(ICookingArtifact):
    def __init__(self):
        '''print("GrillArtifact initialized")'''
        self.state = "raw"

    def cook(self, minutes):
        '''print(f"Cooking for {minutes} minutes in the grill")'''
        if minutes < 4:
            self.state = "rare"
        elif 4 <= minutes < 6:
            self.state = "medium"
        elif 6 <= minutes < 9:
            self.state = "medium well"
        elif 9 <= minutes < 12:
            self.state = "well done"
        else:
            self.state = "burnt"
        return f"Grilled for {minutes} minutes."

    def get_cooking_state(self):
        '''print("Getting cooking state from the grill.")'''
        return self.state