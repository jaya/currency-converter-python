from pydantic import BaseModel, Field, field_validator


def validate_currency(value: str) -> str:
    allowed_currencies = ["BRL", "USD", "EUR", "JPY"]
    if value not in allowed_currencies:
        raise ValueError(f"Suported currencies are {allowed_currencies}")
    return value


class Convert(BaseModel):

    value: float = Field(ge=0, title="The value to convert")
    from_currency: str
    to_currency: str
    user_id: int = Field(ge=0, title="User ID", description="The user ID")

    @field_validator("from_currency")
    @classmethod
    def validate_from_currency(cls, value: str) -> str:
        return validate_currency(value)

    @field_validator("to_currency")
    @classmethod
    def validate_to_currency(cls, value: str) -> str:
        return validate_currency(value)
