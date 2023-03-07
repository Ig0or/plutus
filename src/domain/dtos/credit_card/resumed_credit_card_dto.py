# Standard
from typing_extensions import NotRequired, TypedDict

from http import HTTPStatus


class ResumedCreditCardDto(TypedDict):
    number: str
    brand: str


class ResumedCreditCardResponseDto(TypedDict):
    result: list[ResumedCreditCardDto]
    message: NotRequired[str]
    success: bool
    status_code: HTTPStatus
