# Local
from abc import abstractmethod
from typing import NoReturn

# Local
from src.domain.models.credit_card.credit_card_model import CreditCardModel


class ICreditCardRepository:
    @staticmethod
    @abstractmethod
    async def get_all_credit_cards() -> list[dict]:
        pass

    @staticmethod
    @abstractmethod
    async def save_new_credit_card(credit_card_model: CreditCardModel) -> NoReturn:
        pass
