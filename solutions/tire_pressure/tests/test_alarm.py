import pytest
from expects import expect, be_false, be_true

from solutions.tire_pressure.src.alarm import Alarm
from solutions.tire_pressure.tests.stub_sensor import StubSensor

CORRECT_PRESSURE = 20
HIGH_PRESSURE = 22
LOW_PRESSURE = 16


class TestAlarm:

    def test_alarm_is_off_by_default(self):
        alarm = Alarm()

        expect(alarm.is_alarm_on).to(be_false)

    @pytest.mark.parametrize("pressure_read", [LOW_PRESSURE, HIGH_PRESSURE])
    def test_alarm_is_on_when_pressure_is_not_between_thresholds(self, pressure_read):
        sensor = StubSensor(pressure_read=pressure_read)
        alarm = Alarm(sensor=sensor)

        alarm.check_pressure()

        expect(alarm.is_alarm_on).to(be_true)

    def test_alarm_is_off_when_pressure_is_in_threshold(self):
        sensor = StubSensor(pressure_read=CORRECT_PRESSURE)
        alarm = Alarm(sensor=sensor)

        alarm.check_pressure()

        expect(alarm.is_alarm_on).to(be_false)
