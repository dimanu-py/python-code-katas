from expects import expect, raise_error

from trip_service.src.exceptions import UserNotLoggedInException
from trip_service.src.service import TripService
from trip_service.src.user import User


class SeamTripService(TripService):

    def __init__(self, user: User | None) -> None:
        self.user = user

    def get_logged_user(self) -> User:
        return self.user


class TestTripService:

    GUEST_USER = None

    def test_user_needs_to_be_logged_in(self):
        trip_service = SeamTripService(self.GUEST_USER)

        expect(lambda: trip_service.get_trips_by_user(self.GUEST_USER)).to(raise_error(UserNotLoggedInException))
