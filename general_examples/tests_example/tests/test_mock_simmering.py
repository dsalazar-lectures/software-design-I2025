from tests_example.app.pot_cooking_artifact import PotArtifact
from tests_example.app.airfryer_cooking_artifact import AirfryerArtifact
from tests_example.tests.mocked_models.mock_simmering_service import MockSimmeringService

def test_pot_simmering_with_mock_service():
    pot = PotArtifact()

    mock_service = MockSimmeringService(pot)
    pot_result = mock_service.simmering(12)
    assert "Simmering for 12 minutes in the pot." == pot_result
    

def test_airfryer_simmering_with_mock_service():
    air_fryer = AirfryerArtifact()

    mock_service = MockSimmeringService(air_fryer)
    air_fryer_result = mock_service.simmering(12)
    assert "ValueError: Este artefacto no permite cocción a fuego lento" == air_fryer_result