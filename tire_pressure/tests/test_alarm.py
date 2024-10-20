from unittest.mock import patch

import pytest
from expects import expect, be_false, be_true

from tire_pressure.src.alarm import Alarm

CORRECT_PRESSURE = 20
HIGH_PRESSURE = 22
LOW_PRESSURE = 16


class TestAlarm:

    def setup_method(self):
        self.alarm = Alarm()

    def test_alarm_is_off_by_default(self):
        expect(self.alarm.is_alarm_on).to(be_false)

    @pytest.mark.parametrize("pressure_read", [LOW_PRESSURE, HIGH_PRESSURE])
    def test_alarm_is_on_when_pressure_is_not_between_thresholds(self, pressure_read):
        with patch("tire_pressure.src.sensor.Sensor.pop_next_pressure_psi_value") as pressure:
            pressure.return_value = pressure_read
            self.alarm.check_pressure()

            expect(self.alarm.is_alarm_on).to(be_true)

    def test_alarm_is_off_when_pressure_is_in_threshold(self):
        with patch("tire_pressure.src.sensor.Sensor.pop_next_pressure_psi_value") as preesure:
            preesure.return_value = CORRECT_PRESSURE
            self.alarm.check_pressure()

            expect(self.alarm.is_alarm_on).to(be_false)