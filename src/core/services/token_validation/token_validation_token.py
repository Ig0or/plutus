# Standard
from abc import abstractmethod


class ITokenValidationService:
    @classmethod
    @abstractmethod
    def validate_token(cls, token: str) -> bool:
        pass
