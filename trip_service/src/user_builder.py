from trip_service.src.trip import Trip
from trip_service.src.user import User


class UserBuilder:

    trips: list[Trip]
    friends: list[User]

    def __init__(self) -> None:
        self.friends = []
        self.trips = []

    def friend_of(self, *friends: User) -> "UserBuilder":
        self.friends = list(friends)
        return self

    def build(self) -> User:
        user = User()

        for friend in self.friends:
            user.add_friend(friend)

        return user
