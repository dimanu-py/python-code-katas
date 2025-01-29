from solutions.trip_service.src.exceptions import UserNotLoggedInException
from solutions.trip_service.src.trip import Trip, TripRepository
from solutions.trip_service.src.user import User


class TripService:

    def __init__(self, repository: TripRepository) -> None:
        self.repository = repository
        self.no_trips = []

    def get_trips_by_user(self, logged_user: User, requested_user: User) -> list[Trip]:
        self._verify(logged_user)

        return self.repository.find_trips_of(requested_user) if requested_user.is_friend_with(logged_user) else self.no_trips

    @staticmethod
    def _verify(logged_user: User) -> None:
        if not logged_user:
            raise UserNotLoggedInException()
