from expects import be_empty, expect, equal

from trip_service.src.trip import Trip
from trip_service.src.user import User
from trip_service.src.user_builder import UserBuilder


class TestUserBuilder:

    ANY_USER = User()
    ANY_TRIP = Trip()

    def test_user_has_no_friends_nor_trips_initially(self):
        builder = UserBuilder()

        user = builder.build()

        expect(user.friends).to(be_empty)
        expect(user.trips).to(be_empty)

    def test_user_has_friends(self):
        builder = UserBuilder()

        user = builder.friend_of(self.ANY_USER).build()

        expect(user.friends).to(equal([self.ANY_USER]))

    def test_user_has_trips(self):
        builder = UserBuilder()

        user = builder.has_travel_to(self.ANY_TRIP).build()

        expect(user.trips).to(equal([self.ANY_TRIP]))
