# Third Party
from pydantic import BaseModel


class CreditCardModel(BaseModel):
    exp_date: str
    holder: str
    number: str
    cvv: str
    brand: str


class CreditCardResponseModel(BaseModel):
    result: CreditCardModel
