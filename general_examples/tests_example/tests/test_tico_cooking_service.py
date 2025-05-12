from tests_example.app.models.noise_artifact import NoiseArtifact
from tests_example.app.models.tico_cooking_service import TicoCookingService
from tests_example.app.models.recipe import Recipe

def test_tico_cooking_service_cooks(monkeypatch):
    monkeypatch.setattr(
        "random.choice",
        lambda frases: "¡Pura vida, quedó tuanis!"
    )

    artifact = NoiseArtifact()
    recipe = Recipe([artifact])
    service = TicoCookingService(artifact)

    result = service.cook_recipe(recipe, 5)
    assert result == ["Cocinado por 5 minutos. ¡Pura vida, quedó tuanis!"]

def test_tico_cooking_service_state():
    artifact = NoiseArtifact()
    service = TicoCookingService(artifact)

    state = service.get_cooking_state()
    assert state == "Listo y con sabor tico"
