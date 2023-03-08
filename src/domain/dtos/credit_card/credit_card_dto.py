# Standard
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CreditCardDto(TypedDict):
    exp_date: str
    holder: str
    number: str
    cvv: Optional[str]
    brand: str


class CreditCardResponseDto(TypedDict):
    result: CreditCardDto
    message: NotRequired[str]
    success: bool
    status_code: int
