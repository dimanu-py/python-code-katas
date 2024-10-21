from expects import be_empty, expect

from trip_service.src.user_builder import UserBuilder


class TestUserBuilder:

    def test_user_has_no_friends_nor_trips_initially(self):
        builder = UserBuilder()

        user = builder.build()

        expect(user.friends).to(be_empty)
        expect(user.trips).to(be_empty)
