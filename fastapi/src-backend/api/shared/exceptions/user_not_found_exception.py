class UserNotFoundException(Exception):
    def __init__(self) -> None:
        self.message: str = 'User not found'
        super().__init__(self.message)
