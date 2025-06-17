class ControlPanel:
    def __init__(self, artifacts):
        """
        artifacts: lista de objetos que implementan ICookingArtifact
        """
        self.artifacts = artifacts
        self.state = "New"
        self.minTemperature = 100
        self.maxTemperature = 500

    def set_all_temperatures(self, temperature: float):
        if temperature < self.minTemperature or temperature > self.maxTemperature:
            raise ValueError(f'La temperatura {temperature}° está fuera del rango de temperaturas permitido {self.minTemperature}° - {self.maxTemperature}°')
        i = 0
        for artifact in self.artifacts:
            artifact.temperature = temperature
            i += 1

