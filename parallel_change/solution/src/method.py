import warnings
import functools


def deprecated(func):
    """Marks a functions as deprecated.

    Prints a warning being emitted when the function is used.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        warnings.warn(f"Function {func.__name__} is deprecated. Will be substituted by is_authenticated_with_role", category=DeprecationWarning, stacklevel=2)
        return func(*args, **kwargs)
    return wrapper


class AuthenticationService:

    def is_authenticated_with_role(self, role: str, user_id: int) -> bool:
        if role == "admin":
            return user_id == 12345
        return False

class AuthenticationClient:
    def __init__(self, authentication_service: AuthenticationService) -> None:
        self.authentication_service = authentication_service

    def run(self) -> None:
        authenticated = self.authentication_service.is_authenticated_with_role("user", 33)
        print("is authenticated: ", str(authenticated))


class YetAnotherClient:
    def run(self) -> bool:
        return AuthenticationService().is_authenticated_with_role("user", 100)


if __name__ == "__main__":
    client = AuthenticationClient(AuthenticationService())
    client.run()