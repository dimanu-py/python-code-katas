from trip_service.src.service import TripService
from trip_service.src.user import User


class SeamTripService(TripService):

    def get_logged_user(self) -> User:
        return None


class TestTripService:
    pass