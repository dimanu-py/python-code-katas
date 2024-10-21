from trip_service.src.exceptions import UserNotLoggedInException
from trip_service.src.trip import Trip, TripRepository
from trip_service.src.user import User
from trip_service.src.user_session import UserSession


class TripService:

    def get_trips_by_user(self, user: User) -> list[Trip]:
        logged_user = self.get_logged_user()
        self._verify(logged_user)

        return self.get_trips_from(user) if user.is_friend_with(logged_user) else []

    @staticmethod
    def _verify(logged_user: User) -> None:
        if not logged_user:
            raise UserNotLoggedInException()

    def get_trips_from(self, user: User) -> list[Trip]:
        return TripRepository.find_trips_by_user(user)

    def get_logged_user(self) -> User:
        return UserSession.get_instance().get_logged_user()
