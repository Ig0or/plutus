# Standard
from http import HTTPStatus
from typing import Callable, NoReturn

# Third Party
from fastapi import Response

# Local
from src.domain.dtos.abstract_response.abstract_response_dto import AbstractResponseDto
from src.domain.dtos.response.response_dto import ResponseDto
from src.domain.exceptions.exceptions import InvalidToken
from src.services.token_validation.token_validation_token import TokenValidationService


class CreditCardEntryPoint:
    @staticmethod
    async def __process_callback(
        callback: Callable, arguments: dict = None
    ) -> AbstractResponseDto:
        response = await callback(**arguments or dict())

        return response

    @staticmethod
    def __validate_header_token(token: str) -> NoReturn:
        valid_token = TokenValidationService.validate_token(token=token)

        if not valid_token:
            raise InvalidToken()

        return

    @staticmethod
    async def process_request(
        callback: Callable, header: str, body_parameters: dict = None
    ) -> Response:
        response_dto = None

        try:
            CreditCardEntryPoint.__validate_header_token(token=header)

            response = await CreditCardEntryPoint.__process_callback(
                callback=callback, arguments=body_parameters
            )

            response_dto = ResponseDto(
                success=response.get("success"),
                status_code=response.get("status_code"),
                message=response.get("message"),
                result=response.get("result"),
            )

        except InvalidToken:
            response_dto = ResponseDto(
                success=False,
                status_code=HTTPStatus.UNAUTHORIZED,
                message="The x-token is invalid.",
            )

        except Exception as exception:
            response_dto = ResponseDto(
                success=False,
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                message="An expected error occurred.",
            )

        finally:
            http_response = response_dto.build_http_response()

            return http_response
