# Third Party
from decouple import config

# Local
from src.services.token_validation.token_validation_service import (
    TokenValidationService,
)


def test_validate_token_when_token_is_valid_then_return_true():
    is_token_valid = TokenValidationService.validate_token(token=config("VALID_TOKEN"))

    assert is_token_valid == True


def test_validate_token_when_token_is_invalid_then_return_false():
    is_token_valid = TokenValidationService.validate_token(token="invalid token")

    assert is_token_valid == False
