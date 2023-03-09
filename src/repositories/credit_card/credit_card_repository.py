# Local
from typing import NoReturn

# Local
from src.core.repositories.credit_card.i_credit_card_repository import (
    ICreditCardRepository,
)
from src.domain.models.credit_card.credit_card_model import CreditCardModel
from src.infrastructure.mongodb.mongodb_infrastructure import MongoDBInfrastructure


class CreditCardRepository(ICreditCardRepository):
    @staticmethod
    async def get_all_credit_cards() -> list[dict]:
        connection = MongoDBInfrastructure.get_connection()

        credit_cards = connection.find({}, {"_id": 0})
        credit_cards_list = list(credit_cards)

        return credit_cards_list

    @staticmethod
    async def save_new_credit_card(credit_card_model: CreditCardModel) -> NoReturn:
        connection = MongoDBInfrastructure.get_connection()

        connection.insert_one(document=credit_card_model)

        return
