# Standard
from unittest.mock import patch

# Third Party
from cryptography.fernet import Fernet
import pytest

# Local
from src.services.obfuscate_data.obfuscate_data_service import ObfuscateDataService
from tests.services.obfuscate_data.stubs import (
    encoded_decrypted_stub,
    encoded_encrypted_stub,
    invalid_type_number_stub,
    valid_encrypted_stub,
    valid_type_number_stub,
)


@patch.object(Fernet, "encrypt", return_value=encoded_encrypted_stub)
def test_obfuscate_value_when_value_is_valid_then_return_encrypted_string(fernet_mock):
    encrypted_value = ObfuscateDataService.obfuscate_value(value=valid_type_number_stub)

    assert len(encrypted_value) == 120
    assert type(encrypted_value) == str


def test_obfuscate_value_when_value_is_invalid_then_raise_attribute_error():
    with pytest.raises(AttributeError):
        ObfuscateDataService.obfuscate_value(value=invalid_type_number_stub)


@patch.object(Fernet, "decrypt", return_value=encoded_decrypted_stub)
def test_deobfuscate_value_when_value_is_valid_then_return_decrypted_string(
    fernet_mock,
):
    decrypted_value = ObfuscateDataService.deobfuscate_value(value=valid_encrypted_stub)

    assert decrypted_value == valid_type_number_stub


def test_deobfuscate_value_when_value_is_invalid_then_raise_attribute_error():
    with pytest.raises(AttributeError):
        ObfuscateDataService.deobfuscate_value(value=invalid_type_number_stub)
