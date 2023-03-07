# Local
from src.infrastructure.mongodb.mongodb_infrastructure import MongoDBInfrastructure


class CreditCardRepository:
    @staticmethod
    async def get_all_credit_cards() -> list[dict]:
        connection = MongoDBInfrastructure.get_connection()

        credit_cards = connection.find()
        credit_cards_list = list(credit_cards)

        return credit_cards_list
