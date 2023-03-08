# Standard
from http import HTTPStatus
from typing import Callable, NoReturn

# Third Party
from fastapi import Response
import loglifos

# Local
from src.domain.dtos.abstract_response.abstract_response_dto import AbstractResponseDto
from src.domain.dtos.response.response_dto import ResponseDto
from src.domain.exceptions.exceptions import (
    CreditCardAlreadyExists,
    CreditCardNotExists,
    InvalidToken,
)
from src.services.token_validation.token_validation_token import TokenValidationService


class CreditCardEntryPoint:
    @staticmethod
    async def __process_callback(
        callback: Callable, parameters: any = None
    ) -> AbstractResponseDto:
        response = await callback(parameters)

        return response

    @staticmethod
    def __validate_header_token(token: str) -> NoReturn:
        valid_token = TokenValidationService.validate_token(token=token)

        if not valid_token:
            raise InvalidToken()

        return

    @staticmethod
    async def process_request(
        callback: Callable, header: str, parameters: any = None
    ) -> Response:
        response_dto = None

        try:
            CreditCardEntryPoint.__validate_header_token(token=header)

            response = await CreditCardEntryPoint.__process_callback(
                callback=callback, parameters=parameters
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

            loglifos.warning(msg="Invalid header token", token=header)

        except CreditCardAlreadyExists:
            response_dto = ResponseDto(
                success=False,
                status_code=HTTPStatus.OK,
                message="This credit card can't be saved because it's already saved.",
            )

            loglifos.warning(
                msg="The credit card wasn't saved because this number is already saved."
            )

        except CreditCardNotExists:
            response_dto = ResponseDto(
                success=False,
                status_code=HTTPStatus.OK,
                message="This credit card doesn't exist.",
            )

            loglifos.warning(msg="The credit card doesn't exist.")

        except Exception as exception:
            response_dto = ResponseDto(
                success=False,
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                message="An unexpected error occurred.",
            )

            loglifos.error(
                msg="An unexpected exception was raised", exception=exception
            )

        finally:
            http_response = response_dto.build_http_response()

            return http_response
