# Standard
from abc import abstractmethod
from typing import NoReturn

# Local
from src.domain.dtos.credit_card.credit_card_dto import CreditCardDto
from src.domain.dtos.credit_card.resumed_credit_card_dto import ResumedCreditCardDto
from src.domain.validators.credit_card.credit_card_validator import CreditCardValidator


class ICreditCardService:
    @staticmethod
    @abstractmethod
    async def list_credit_cards() -> list[ResumedCreditCardDto]:
        pass

    @staticmethod
    @abstractmethod
    async def detail_credit_card(credit_card_number: str) -> CreditCardDto:
        pass

    @staticmethod
    @abstractmethod
    async def create_credit_card(credit_card: CreditCardValidator) -> NoReturn:
        pass
