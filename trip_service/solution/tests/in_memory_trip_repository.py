from trip_service.solution.src.trip import TripRepository, Trip
from trip_service.solution.src.user import User


class InMemoryTripRepository(TripRepository):

    @staticmethod
    def find_trips_of(user: User) -> list[Trip]:
        return user.trips
