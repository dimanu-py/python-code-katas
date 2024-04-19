

class AuthenticationService:
    def is_authenticated(self, _id: int) -> bool:
        return _id == 12345

    '''
    the goal is to replace the method above with this one:
    def is_authenticated(self, role, id):
        return id == 12345
    '''


class AuthenticationClient:
    def __init__(self, authentication_service: AuthenticationService) -> None:
        self.authentication_service = authentication_service

    def run(self) -> None:
        authenticated = self.authentication_service.is_authenticated(33)
        print("is authenticated: ", str(authenticated))


class YetAnotherClient:
    def run(self) -> bool:
        return AuthenticationService().is_authenticated(100)


if __name__ == "__main__":
    client = AuthenticationClient(AuthenticationService())
    client.run()