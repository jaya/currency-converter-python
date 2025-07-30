from pydantic import BaseModel, Field, field_validator


def validate_currency(value: str) -> str:
    allowed_currencies = ["BRL", "USD", "EUR", "JPY"]
    if value not in allowed_currencies:
        raise ValueError(f"Suported currencies are {allowed_currencies}")
    return value


class TransactionRequest(BaseModel):

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


class TransactionResponse(BaseModel):
    transaction_id: int = Field(
        title="Transaction ID", description="The transaction ID"
    )
    user_id: int = Field(title="User ID", description="The user ID")
    from_currency: str = Field(title="From Currency", description="The From Currency")
    to_currency: str = Field(title="To Currency", description="The To Currency")
    from_value: float = Field(title="From Value", description="The From Value")
    to_value: float = Field(title="To Value", description="The To Value")
    rate: float = Field(title="Rate", description="The Rate")
    timestamp: str = Field(title="Timestamp", description="The Timestamp")
