# Standard
from unittest.mock import patch

# Third Party
import pytest

# Local
from src.domain.exceptions.exceptions import (
    CreditCardAlreadyExists,
    CreditCardNotExists,
)
from src.repositories.credit_card.credit_card_repository import CreditCardRepository
from src.services.credit_card.credit_card_service import CreditCardService
from tests.services.credit_card.stubs import (
    credit_card_dto_stub,
    credit_card_model_stub,
    credit_card_validator_stub,
    decrypted_credit_cards_models_stub,
    existing_credit_card_validator_stub,
    invalid_credit_cred_number_stub,
    resumed_credit_cards_dto_stub,
    valid_credit_cred_number_stub,
)


@patch.object(
    CreditCardService,
    "_CreditCardService__get_all_credit_cards",
    return_value=decrypted_credit_cards_models_stub,
)
async def test_list_credit_cards_when_connection_is_open_then_return_resumed_credit_cards_dto(
    credit_card_service_mock,
):
    resumed_credit_cards_dto = await CreditCardService.list_credit_cards()

    assert resumed_credit_cards_dto == resumed_credit_cards_dto_stub


@patch.object(
    CreditCardService,
    "_CreditCardService__get_all_credit_cards",
    return_value=decrypted_credit_cards_models_stub,
)
async def test_detail_credit_card_when_credit_card_number_is_valid_then_return_credit_card_dto(
    credit_card_service_mock,
):
    credit_card_dto = await CreditCardService.detail_credit_card(
        credit_card_number=valid_credit_cred_number_stub
    )

    assert credit_card_dto == credit_card_dto_stub


@patch.object(
    CreditCardService,
    "_CreditCardService__get_all_credit_cards",
    return_value=decrypted_credit_cards_models_stub,
)
async def test_detail_credit_card_when_credit_card_number_is_invalid_then_raise_credit_card_not_exists_exception(
    credit_card_service_mock,
):
    with pytest.raises(CreditCardNotExists):
        await CreditCardService.detail_credit_card(
            credit_card_number=invalid_credit_cred_number_stub
        )


@patch.object(
    CreditCardService,
    "_CreditCardService__get_all_credit_cards",
    return_value=decrypted_credit_cards_models_stub,
)
@patch.object(CreditCardRepository, "save_new_credit_card")
async def test_create_credit_card_when_credit_card_input_is_valid_then_save_the_credit_card(
    credit_card_repository_mock, credit_card_service_mock
):
    await CreditCardService.create_credit_card(credit_card=credit_card_validator_stub)

    credit_card_repository_mock.assert_called_with(
        credit_card_model=credit_card_model_stub
    )


@patch.object(
    CreditCardService,
    "_CreditCardService__get_all_credit_cards",
    return_value=decrypted_credit_cards_models_stub,
)
@patch.object(CreditCardRepository, "save_new_credit_card")
async def test_create_credit_card_when_credit_card_input_already_exists_then_raise_credit_card_already_exists_exception(
    credit_card_repository_mock, credit_card_service_mock
):
    with pytest.raises(CreditCardAlreadyExists):
        await CreditCardService.create_credit_card(
            credit_card=existing_credit_card_validator_stub
        )

    credit_card_repository_mock.assert_not_called()
