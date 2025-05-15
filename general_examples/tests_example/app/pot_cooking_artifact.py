from tests_example.app.i_simmering_capable_artifact import ISimmeringCapableArtifact


class PotArtifact(ISimmeringCapableArtifact):
    def __init__(self):
        self.time_cooked = 0
        print("PotArtifact initialized")

    def cook(self, minutes: int) -> str:
        self.time_cooked += minutes
        return f"Cooking for {minutes} minutes in the pot."

    def simmer(self, minutes: int) -> str:
        self.time_cooked += minutes
        return f"Simmering for {minutes} minutes in the pot."

    def get_cooking_state(self) -> str:
        if self.time_cooked < 10:
            return "raw"
        elif self.time_cooked < 20:
            return "cooked"
        else:
            return "overcooked"
