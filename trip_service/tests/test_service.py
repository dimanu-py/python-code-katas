from expects import expect, raise_error, be_empty, equal

from trip_service.src.exceptions import UserNotLoggedInException
from trip_service.src.service import TripService
from trip_service.src.trip import Trip
from trip_service.src.user import User


class SeamTripService(TripService):

    def __init__(self, user: User | None) -> None:
        self.user = user

    def get_logged_user(self) -> User:
        return self.user

    def get_trips_from(self, user: User) -> list[Trip]:
        return user.get_trips()


class TestTripService:

    GUEST_USER = None
    LOGGED_USER = User()
    GENERIC_USER = User()
    CANADA_TRIP = Trip()

    def test_user_needs_to_be_logged_in(self):
        trip_service = SeamTripService(self.GUEST_USER)

        expect(lambda: trip_service.get_trips_by_user(self.GENERIC_USER)).to(raise_error(UserNotLoggedInException))

    def test_logged_user_gets_no_trips_if_is_not_friend(self):
        trip_service = SeamTripService(self.LOGGED_USER)
        stranger = User()
        stranger.add_friend(self.GENERIC_USER)

        trips = trip_service.get_trips_by_user(stranger)

        expect(trips).to(be_empty)

    def test_logged_user_gets_friend_trips(self):
        friend = User()
        friend.add_friend(self.LOGGED_USER)
        friend.add_friend(self.GENERIC_USER)
        friend.add_trip(self.CANADA_TRIP)
        trip_service = SeamTripService(self.LOGGED_USER)

        trips = trip_service.get_trips_by_user(friend)

        expect(trips).to(equal([self.CANADA_TRIP]))