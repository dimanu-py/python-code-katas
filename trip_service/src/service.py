from trip_service.src.exceptions import UserNotLoggedInException
from trip_service.src.trip import Trip, TripRepository
from trip_service.src.user import User
from trip_service.src.user_session import UserSession


class TripService:

    def __init__(self, repository: TripRepository) -> None:
        self.repository = repository

    def get_trips_by_user(self, logged_user: User, requested_user: User) -> list[Trip]:
        self._verify(logged_user)

        return self.repository.find_trips_by_user(requested_user) if requested_user.is_friend_with(logged_user) else []

    @staticmethod
    def _verify(logged_user: User) -> None:
        if not logged_user:
            raise UserNotLoggedInException()
