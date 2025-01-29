from solutions.trip_service.src.trip import TripRepository, Trip
from solutions.trip_service.src.user import User


class InMemoryTripRepository(TripRepository):

    @staticmethod
    def find_trips_of(user: User) -> list[Trip]:
        return user.trips
