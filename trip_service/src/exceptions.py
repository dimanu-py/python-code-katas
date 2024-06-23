

class TripServiceError(Exception):
    pass


class DependendClassCallDuringUnitTestException(TripServiceError):
    pass


class UserNotLoggedInException(TripServiceError):
  pass
