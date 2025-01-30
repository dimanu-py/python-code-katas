from expects import be_empty, expect, equal

from trip_service.solution.src.trip import Trip
from trip_service.solution.src.user import User
from trip_service.solution.src.user_builder import UserBuilder


class TestUserBuilder:

    ANY_USER = User()
    ANY_TRIP = Trip()

    def setup_method(self):
        self.builder = UserBuilder()

    def test_user_has_no_friends_nor_trips_initially(self):
        user = self.builder.build()

        expect(user.friends).to(be_empty)
        expect(user.trips).to(be_empty)

    def test_user_has_friends(self):
        user = self.builder.friend_of(self.ANY_USER).build()

        expect(user.friends).to(equal([self.ANY_USER]))

    def test_user_has_trips(self):
        user = self.builder.has_travel_to(self.ANY_TRIP).build()

        expect(user.trips).to(equal([self.ANY_TRIP]))
