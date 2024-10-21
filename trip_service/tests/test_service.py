from expects import expect, raise_error, be_empty, equal

from trip_service.src.exceptions import UserNotLoggedInException
from trip_service.src.service import TripService
from trip_service.src.trip import Trip
from trip_service.src.user import User
from trip_service.src.user_builder import UserBuilder


class SeamTripService(TripService):

    def get_trips_from(self, user: User) -> list[Trip]:
        return user.get_trips()


class TestTripService:

    GUEST_USER = None
    LOGGED_USER = User()
    GENERIC_USER = User()
    CANADA_TRIP = Trip()

    def test_user_needs_to_be_logged_in(self):
        trip_service = SeamTripService()

        expect(lambda: trip_service.get_trips_by_user(self.GUEST_USER, self.GENERIC_USER)).to(raise_error(UserNotLoggedInException))

    def test_logged_user_gets_no_trips_if_is_not_friend(self):
        trip_service = SeamTripService()
        stranger = UserBuilder().friend_of(self.GENERIC_USER).build()

        trips = trip_service.get_trips_by_user(self.LOGGED_USER, stranger)

        expect(trips).to(be_empty)

    def test_logged_user_gets_friend_trips(self):
        trip_service = SeamTripService()
        friend = (UserBuilder()
                  .friend_of(self.LOGGED_USER, self.GENERIC_USER)
                  .has_travel_to(self.CANADA_TRIP)
                  .build())

        trips = trip_service.get_trips_by_user(self.LOGGED_USER, friend)

        expect(trips).to(equal([self.CANADA_TRIP]))