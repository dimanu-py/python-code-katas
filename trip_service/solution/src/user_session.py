from trip_service.solution.src.exceptions import DependendClassCallDuringUnitTestException
from trip_service.solution.src.user import User


class UserSession:

    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super(UserSession, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def get_instance() -> 'UserSession':
        return UserSession()

    def is_user_logged_in(self, user: User) -> bool:
        raise DependendClassCallDuringUnitTestException(
            "UserSession.isUserLoggedIn() should not be called in an unit test"
        )

    def get_logged_user(self) -> User:
        raise DependendClassCallDuringUnitTestException(
            "UserSession.getLoggedUser() should not be called in an unit test"
        )


