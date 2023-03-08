# Standard
from http import HTTPStatus

# Local
from src.domain.dtos.abstract_response.abstract_response_dto import AbstractResponseDto
from src.domain.dtos.credit_card.credit_card_dto import CreditCardResponseDto
from src.domain.dtos.credit_card.resumed_credit_card_dto import (
    ResumedCreditCardResponseDto,
)
from src.domain.validators.credit_card.credit_card_validator import CreditCardValidator
from src.services.credit_card.credit_card_service import CreditCardService


class CreditCardController:
    @staticmethod
    async def list_credit_cards(*args) -> ResumedCreditCardResponseDto:
        result = await CreditCardService.list_credit_cards()

        response: ResumedCreditCardResponseDto = {
            "result": result,
            "success": True,
            "status_code": HTTPStatus.OK,
        }

        return response

    @staticmethod
    async def detail_credit_card(credit_card_number: str) -> CreditCardResponseDto:
        result = await CreditCardService.detail_credit_card(
            credit_card_number=credit_card_number
        )

        response: CreditCardResponseDto = {
            "result": result,
            "success": True,
            "status_code": HTTPStatus.OK,
        }

        return response

    @staticmethod
    async def create_credit_card(
        credit_card: CreditCardValidator,
    ) -> AbstractResponseDto:
        await CreditCardService.create_credit_card(credit_card=credit_card)

        response: AbstractResponseDto = {
            "message": "The credit card was saved.",
            "success": True,
            "status_code": HTTPStatus.CREATED,
        }

        return response
