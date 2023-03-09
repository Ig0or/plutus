# Third Party
import pytest

# Local
from src.services.obfuscate_data.obfuscate_data_service import ObfuscateDataService
from tests.services.obfuscate_data.stubs import (
    invalid_type_number_stub,
    valid_encrypted_stub,
    valid_type_number_stub,
)


def test_obfuscate_value_when_value_is_valid_then_return_encrypted_string():
    encrypted_value = ObfuscateDataService.obfuscate_value(value=valid_type_number_stub)

    assert len(encrypted_value) == 120
    assert type(encrypted_value) == str


def test_obfuscate_value_when_value_is_invalid_then_raise_attribute_error():
    with pytest.raises(AttributeError):
        ObfuscateDataService.obfuscate_value(value=invalid_type_number_stub)


def test_deobfuscate_value_when_value_is_valid_then_return_decrypted_string():
    decrypted_value = ObfuscateDataService.deobfuscate_value(value=valid_encrypted_stub)

    assert decrypted_value == valid_type_number_stub


def test_deobfuscate_value_when_value_is_invalid_then_raise_attribute_error():
    with pytest.raises(AttributeError):
        ObfuscateDataService.deobfuscate_value(value=invalid_type_number_stub)
