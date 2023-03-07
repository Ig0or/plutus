# Local
from src.domain.dtos.credit_card.resumed_credit_card_dto import ResumedCreditCardDto
from src.domain.extensions.credit_card.credit_card_extension import CreditCardExtension
from src.repositories.credit_card.credit_card_repository import CreditCardRepository


class CreditCardService:
    @staticmethod
    async def list_credit_cards() -> list[ResumedCreditCardDto]:
        credit_cards_list = await CreditCardRepository.get_all_credit_cards()

        credit_cards_model = CreditCardExtension.to_array_credit_card_model(
            credit_cards=credit_cards_list
        )
        resumed_credit_cards_dto = CreditCardExtension.to_array_resumed_credit_card_dto(
            credit_cards_model=credit_cards_model
        )

        return resumed_credit_cards_dto
