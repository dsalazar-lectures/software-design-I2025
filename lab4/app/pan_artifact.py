from lab4.app.i_cooking_artifact import ICookingArtifact

class PanArtifact(ICookingArtifact):
    def __init__(self):
        print("PanArtifact initialized")
        self.state = "new"

    def grease(self, type_of_grease):
        if type_of_grease == "oil" or type_of_grease == "animal fat" or type_of_grease == "butter":
            print(f"Greasing the pan with {type_of_grease}.")
            self.state = "greased"
        else:
            print(f"Cannot grease the pan with {type_of_grease}.")

    def cook(self, minutes):
        if self.state == "greased":
            print(f"Cooking for {minutes} minutes in the pan.")
            self.state = "cooked"
        else:
            print("You forgot to grease the pan, the food's going to burn.")
            self.state = "burnt"

    def get_cooking_state(self):
        print("Getting cooking state from the pan.")
        return self.state