class Recipe:
    def __init__(self, artifacts, seasonings=None):
        """
        artifacts: lista de objetos que implementan ICookingArtifact
        seasonings: Lista de sazonadores que implementan ICookingSeasoning 
        """
        self.artifacts = artifacts
        self.seasonings = seasonings
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
    
    def add_all_seasonings(self):
        results = []
        if self.seasonings:
            for seasoning in self.seasonings:
                result = seasoning.add()
                results.append(result)
        return results
    
    def get_all_seasonings_states(self):
        states = []
        if self.seasonings:
            for seasoning in self.seasonings:
                state = seasoning.get_seasonig_state()
                states.append(state)
        return states
