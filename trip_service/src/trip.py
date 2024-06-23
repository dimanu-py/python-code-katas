from trip_service.src.exceptions import DependendClassCallDuringUnitTestException
from trip_service.src.user import User


class Trip:
  pass


class TripRepository:
  @staticmethod
  def find_trips_by_user(user: User) -> list[Trip]:
    raise DependendClassCallDuringUnitTestException("TripDAO should not be invoked on an unit test.")