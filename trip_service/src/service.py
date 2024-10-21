from trip_service.src.exceptions import UserNotLoggedInException
from trip_service.src.trip import Trip, TripRepository
from trip_service.src.user import User
from trip_service.src.user_session import UserSession


class TripService:

    def get_trips_by_user(self, user: User) -> list[Trip]:
        logged_user = self.get_logged_user()
        is_friend = False
        trip_list = []
        if logged_user:
          for friend in user.get_friends():
            if friend is logged_user:
              is_friend = True
              break
          if is_friend:
            trip_list = TripRepository.find_trips_by_user(user)
          return trip_list
        else:
            raise UserNotLoggedInException()

    def get_logged_user(self) -> User:
        return UserSession.get_instance().get_logged_user()
