from expects import expect, be_false

from trip_service.src.user import User


class TestUser:

    def test_user_has_no_friends(self):
        user = User()
        stranger = User()

        expect(user.is_friend_with(stranger)).to(be_false)
