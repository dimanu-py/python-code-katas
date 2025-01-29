from expects import expect, be_false, be_true

from solutions.trip_service.src.user import User


class TestUser:

    def test_user_has_no_friends(self):
        user = User()
        stranger = User()

        expect(user.is_friend_with(stranger)).to(be_false)

    def test_user_has_friends(self):
        user = User()
        friend = User()
        user.add_friend(friend)

        expect(user.is_friend_with(friend)).to(be_true)
