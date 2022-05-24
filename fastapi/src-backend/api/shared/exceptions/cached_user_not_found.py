class CachedUserNotFound(Exception):
    def __init__(self, *args: object) -> None:
        self.message = 'Cached user not found'
        super().__init__(self.message, *args)
