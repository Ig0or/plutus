# Third Party
from decouple import config

# Local
from src.core.services.token_validation.token_validation_token import (
    ITokenValidationService,
)


class TokenValidationService(ITokenValidationService):
    __valid_token = config("VALID_TOKEN")

    @classmethod
    def validate_token(cls, token: str) -> bool:
        is_token_valid = False

        if token == cls.__valid_token:
            is_token_valid = True

        return is_token_valid
