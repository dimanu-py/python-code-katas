from expects import expect, be_false

from tire_pressure.src.alarm import Alarm


class TestAlarm:

    def test_alarm_is_off_by_default(self):
        alarm = Alarm()

        expect(alarm.is_alarm_on).to(be_false)
