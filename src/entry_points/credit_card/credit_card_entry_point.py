# Standard
from typing import Callable

# Third Party
from http import HTTPStatus
from fastapi import Response

# Local
from src.domain.exceptions.exceptions import InvalidToken
from src.domain.models.response.response_model import ResponseModel
from src.services.token_validation.token_validation_token import TokenValidationService


class CreditCardEntryPoint:
    @staticmethod
    async def process_request(
        callback: Callable, header: str, body_parameters: dict = None
    ) -> Response:
        response_model = None

        try:
            valid_token = TokenValidationService.validate_token(token=header)

            if not valid_token:
                raise InvalidToken()

            response_model = callback(**body_parameters)

        except InvalidToken:
            response_model = ResponseModel(
                message="The x-token is invalid.", success=False
            ).build_http_response(status_code=HTTPStatus.UNAUTHORIZED)

        finally:
            return response_model
