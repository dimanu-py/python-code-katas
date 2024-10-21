from trip_service.src.trip import TripRepository, Trip
from trip_service.src.user import User


class InMemoryTripRepository(TripRepository):

    @staticmethod
    def find_trips_by_user(user: User) -> list[Trip]:
        return user.trips
