

class User:

    def __init__(self):
        self.trips: list = []
        self.friends: list[User] = []

    def get_friends(self) -> list["User"]:
        return self.friends

    def add_friend(self, user: "User") -> None:
        self.friends.append(user)

    def add_trip(self, trip) -> None:
        self.trips.append(trip)

    def get_trips(self) -> list:
        return self.trips
