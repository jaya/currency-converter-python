class BaseCustomException(Exception):

    def __init__(self, message) -> None:
        self.message = message


class CurrencyAPIException(BaseCustomException):
    pass


class FailToParseException(BaseCustomException):
    pass


class FailToStoreDataException(BaseCustomException):
    pass
