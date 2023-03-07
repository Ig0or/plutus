# Third Party
from fastapi import APIRouter, Header, Response

# Local
from src.controllers.credit_card.credit_card_controller import CreditCardController
from src.domain.dtos.credit_card.resumed_credit_card_dto import (
    ResumedCreditCardResponseDto,
)
from src.entry_points.credit_card.credit_card_entry_point import CreditCardEntryPoint


class CreditCardRouter:
    __credit_card_router = APIRouter()

    @classmethod
    def get_routers(cls) -> APIRouter:
        return cls.__credit_card_router

    @staticmethod
    @__credit_card_router.get(
        "/api/v1/credit-card", response_model=ResumedCreditCardResponseDto
    )
    async def list_credit_cards(
        x_token: str = Header(default=None, convert_underscores=True)
    ) -> Response:
        response = await CreditCardEntryPoint.process_request(
            callback=CreditCardController.list_credit_cards, header=x_token
        )

        return response
