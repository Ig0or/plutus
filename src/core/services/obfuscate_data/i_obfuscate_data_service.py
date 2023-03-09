# Standard
from abc import abstractmethod


class IObfuscateDataService:
    @classmethod
    @abstractmethod
    def obfuscate_value(cls, value: str) -> str:
        pass

    @classmethod
    @abstractmethod
    def deobfuscate_value(cls, value: str) -> str:
        pass
