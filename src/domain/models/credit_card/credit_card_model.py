# Third Party
from typing import TypedDict, Optional


class CreditCardModel(TypedDict):
    exp_date: str
    holder: str
    number: str
    cvv: Optional[str]
    brand: str
