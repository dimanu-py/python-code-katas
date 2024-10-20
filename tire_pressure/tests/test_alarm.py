from unittest.mock import patch

from expects import expect, be_false, be_true

from tire_pressure.src.alarm import Alarm


class TestAlarm:

    def test_alarm_is_off_by_default(self):
        alarm = Alarm()

        expect(alarm.is_alarm_on).to(be_false)

    def test_alarm_is_on_when_pressure_is_below_threshold(self):
        alarm = Alarm()

        with patch("tire_pressure.src.sensor.Sensor.pop_next_pressure_psi_value") as pressure:
            pressure.return_value = 16
            alarm.check_pressure()

            expect(alarm.is_alarm_on).to(be_true)

    def test_alarm_is_on_when_pressure_is_above_threshold(self):
        alarm = Alarm()

        with patch("tire_pressure.src.sensor.Sensor.pop_next_pressure_psi_value") as pressure:
            pressure.return_value = 22
            alarm.check_pressure()

            expect(alarm.is_alarm_on).to(be_true)