from trip_service.solution.src.trip import Trip
from trip_service.solution.src.user import User


class UserBuilder:

    trips: list[Trip]
    friends: list[User]

    def __init__(self) -> None:
        self.friends = []
        self.trips = []

    def friend_of(self, *friends: User) -> "UserBuilder":
        self.friends = list(friends)
        return self

    def has_travel_to(self, *trips: Trip) -> "UserBuilder":
        self.trips = list(trips)
        return self

    def build(self) -> User:
        user = User()

        for friend in self.friends:
            user.add_friend(friend)
        for trip in self.trips:
            user.add_trip(trip)

        return user
