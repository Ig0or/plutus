# Third Party
from typing import TypedDict


class CreditCardModel(TypedDict):
    id: str
    exp_date: str
    holder: str
    number: str
    cvv: str
    brand: str
