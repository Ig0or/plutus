# Third Party
from decouple import config


class TokenValidationService:
    __valid_token = config("VALID_TOKEN")

    @classmethod
    def validate_token(cls, token: str) -> bool:
        is_token_valid = False

        if token == cls.__valid_token:
            is_token_valid = True

        return is_token_valid
