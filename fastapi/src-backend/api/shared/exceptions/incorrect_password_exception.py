class IncorrectPasswordException(Exception):
    def __init__(self) -> None:
        self.message: str = 'Incorrect Password'
        super().__init__(self.message)
