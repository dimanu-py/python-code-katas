from trip_service.solution.src.exceptions import DependendClassCallDuringUnitTestException
from trip_service.solution.src.user import User


class Trip:
  pass


class TripRepository:
  @staticmethod
  def find_trips_of(user: User) -> list[Trip]:
    raise DependendClassCallDuringUnitTestException("TripDAO should not be invoked on an unit test.")