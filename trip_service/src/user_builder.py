from trip_service.src.trip import Trip
from trip_service.src.user import User


class UserBuilder:

    trips: list[Trip]
    friends: list[User]

    def __init__(self) -> None:
        self.friends = []
        self.trips = []

    def build(self) -> User:
        user = User()

        return user
