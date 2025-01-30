class InvalidTurnError(Exception):

    def __init__(self, player: str) -> None:
        message = f"Player {player} cannot play first"
        super().__init__(message)
