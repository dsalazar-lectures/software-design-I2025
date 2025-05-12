from tests_example.app.i_cooking_artifact import ICookingArtifact
import random

class NoiseArtifact(ICookingArtifact):
    def cook(self, time):
        frases_ticas = [
            "¡Eso quedó como para chuparse los dedos!",
            "Mae, esta vara está a otro nivel.",
            "¡Cuidado y no se le va de más el sabor!",
            "Esto quedó como en casa de la abuela.",
            "¡Pura vida, quedó tuanis!",
        ]
        return f"Cocinado por {time} minutos. {random.choice(frases_ticas)}"

    def get_cooking_state(self):
        return "Listo y con sabor tico"
