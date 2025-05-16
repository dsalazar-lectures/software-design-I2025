class Recipe:
    def __init__(self, artifacts):
        """
        artifacts: lista de objetos que implementan ICookingArtifact
        """
        self.artifacts = artifacts
        self.state = "New"

    def cook_all(self, minutes):
        results = []
        for artifact in self.artifacts:
            result = artifact.cook(minutes)
            results.append(result)
        return results

    def get_all_states(self):
        states = []
        for artifact in self.artifacts:
            state = artifact.get_cooking_state()
            states.append(state)
        return states
