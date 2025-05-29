import random
from tests_example.app.models.noise_artifact import NoiseArtifact

def test_cook_with_noise(monkeypatch):
    monkeypatch.setattr(random, "choice", lambda x: "¡Pura vida, quedó tuanis!")

    artifact = NoiseArtifact()
    result = artifact.cook(5)

    assert result == "Cocinado por 5 minutos. ¡Pura vida, quedó tuanis!"

def test_get_cooking_state():
    artifact = NoiseArtifact()
    assert artifact.get_cooking_state() == "Listo y con sabor tico"
