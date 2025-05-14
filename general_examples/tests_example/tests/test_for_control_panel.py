from tests_example.app.models.control_panel import ControlPanel
from unittest.mock import MagicMock
from unittest import TestCase

class TestsForControlPanel(TestCase):
    def test_set_all_temperatures_works_with_too_low_value(self):
        mock_artifact1 = MagicMock()
        mock_artifact2 = MagicMock()
        control_panel = ControlPanel([mock_artifact1, mock_artifact2])
        temperature_value = control_panel.minTemperature - 0.1
        self.assertRaises(ValueError, control_panel.set_all_temperatures, temperature_value)

    def test_set_all_temperatures_works_with_too_high_value(self):
        mock_artifact1 = MagicMock()
        mock_artifact2 = MagicMock()
        control_panel = ControlPanel([mock_artifact1, mock_artifact2])
        temperature_value = control_panel.maxTemperature + 0.1
        self.assertRaises(ValueError, control_panel.set_all_temperatures, temperature_value)

    def test_set_all_temperatures_works_with_correct_value(self):
        mock_artifact1 = MagicMock()
        mock_artifact2 = MagicMock()
        control_panel = ControlPanel([mock_artifact1, mock_artifact2])
        temperature_value = control_panel.minTemperature
        control_panel.set_all_temperatures(temperature_value)