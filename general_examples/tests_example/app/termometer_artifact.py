from tests_example.app.i_cooking_artifact import ICookingArtifact

class Termometer_Artifact(ICookingArtifact):
    def __init__(self):
        self.doness = ["blue rare","rare","medium rare","medium","well done","burned"]
        self.status = "not even cooked"

    def cook(self, minutes):
        if 1 <= minutes >= 2:
         self.status = self.doness[1]
        elif 2< minutes >= 4:
         self.status = self.doness[2]
        elif 4 < minutes >= 5:
         self.status = self.doness[3]
        elif 5 < minutes >= 7:
            self.status = self.doness[4]
        elif minutes > 8:
           self.status = self.doness[5]
        
        return f"El término del corte de carne es: {self.status}."

    def get_cooking_state(self):
     print("Obteniendo el termino del corte, ojito")
     return self.status