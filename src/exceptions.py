class BaseCustomException(Exception):

    def __init__(self, message: str, status_code: int = 500) -> None:
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)


class CurrencyAPIException(BaseCustomException):
    pass


class FailToParseException(BaseCustomException):
    pass


class FailToStoreDataException(BaseCustomException):
    pass


class TransactionNotFoundException(BaseCustomException):
    def __init__(self, message, status_code: int = 404) -> None:
        self.status_code = status_code
        self.message = message
        super().__init__(self.message, status_code)
