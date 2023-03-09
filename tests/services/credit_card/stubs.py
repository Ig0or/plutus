# Standard
from unittest.mock import ANY

# Local
from src.domain.validators.credit_card.credit_card_validator import CreditCardValidator

decrypted_credit_cards_models_stub = [
    {
        "exp_date": "2023-03-31",
        "holder": "igor",
        "number": "4556427894195721",
        "cvv": "123",
        "brand": "visa",
    },
    {
        "exp_date": "2024-02-29",
        "holder": "igor",
        "number": "30020957332457",
        "cvv": "123",
        "brand": "diners",
    },
]

resumed_credit_cards_dto_stub = [
    {"number": "4556427894195721", "brand": "visa"},
    {"number": "30020957332457", "brand": "diners"},
]

valid_credit_cred_number_stub = "4556427894195721"
invalid_credit_cred_number_stub = "123456"

credit_card_dto_stub = {
    "exp_date": "2023-03-31",
    "holder": "igor",
    "number": "4556427894195721",
    "cvv": "123",
    "brand": "visa",
}

credit_card_validator_stub = CreditCardValidator(
    exp_date="05/2024", holder="igor", number="5467282689421047", cvv="1234"
)
existing_credit_card_validator_stub = CreditCardValidator(
    exp_date="05/2024", holder="igor", number="4556427894195721", cvv="1234"
)

credit_card_model_stub = {
    "exp_date": "2024-05-31",
    "holder": "igor",
    "number": ANY,
    "cvv": "1234",
    "brand": "master",
}
