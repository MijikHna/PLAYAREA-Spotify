class UserTableNotFoundException(Exception):
    def __init__(self) -> None:
        self.message: str = 'No such table'
        super().__init__(self.message)
