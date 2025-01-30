from tire_pressure.solution.src.sensor import Sensor


class StubSensor(Sensor):

    pressure: float

    def __init__(self, pressure_read: float) -> None:
        self.pressure = pressure_read

    def pop_next_pressure_psi_value(self) -> float:
        return self.pressure
