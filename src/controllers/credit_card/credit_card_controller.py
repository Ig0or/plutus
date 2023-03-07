# Standard
from http import HTTPStatus

# Local
from src.domain.dtos.credit_card.resumed_credit_card_dto import (
    ResumedCreditCardResponseDto,
)
from src.services.credit_card.credit_card_service import CreditCardService


class CreditCardController:
    @staticmethod
    async def list_credit_cards(**kwargs) -> ResumedCreditCardResponseDto:
        result = await CreditCardService.list_credit_cards()
        response: ResumedCreditCardResponseDto = {
            "result": result,
            "success": True,
            "status_code": HTTPStatus.OK,
        }

        return response
