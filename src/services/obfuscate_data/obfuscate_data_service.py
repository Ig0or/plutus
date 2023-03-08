# Third Party
from cryptography.fernet import Fernet
from decouple import config


class ObfuscateDataService:
    __fernet_key = config("FERNET_KEY")
    __fernet_instance = Fernet(key=__fernet_key)

    @classmethod
    def obfuscate_value(cls, value: str) -> str:
        encoded_value = value.encode()
        obfuscated_value = cls.__fernet_instance.encrypt(data=encoded_value)
        decoded_value = obfuscated_value.decode()

        return decoded_value

    @classmethod
    def deobfuscate_value(cls, value: str) -> str:
        encoded_value = value.encode()
        deobfuscated_value = cls.__fernet_instance.decrypt(token=encoded_value)
        decoded_value = deobfuscated_value.decode()

        return decoded_value
