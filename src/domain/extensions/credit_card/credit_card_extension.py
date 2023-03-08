# Third Party
from creditcard import CreditCard


# Local
from src.domain.dtos.credit_card.credit_card_dto import CreditCardDto
from src.domain.dtos.credit_card.resumed_credit_card_dto import ResumedCreditCardDto
from src.domain.models.credit_card.credit_card_model import CreditCardModel
from src.domain.validators.credit_card.credit_card_validator import CreditCardValidator


class CreditCardExtension:
    @staticmethod
    def __to_resumed_credit_card_dto(
        credit_card_model: CreditCardModel,
    ) -> ResumedCreditCardDto:
        dto: ResumedCreditCardDto = {
            "number": credit_card_model["number"],
            "brand": credit_card_model["brand"],
        }

        return dto

    @staticmethod
    def to_array_resumed_credit_card_dto(
        credit_cards_model: list[CreditCardModel],
    ) -> list[ResumedCreditCardDto]:
        dtos = list()

        for credit_card in credit_cards_model:
            dto = CreditCardExtension.__to_resumed_credit_card_dto(
                credit_card_model=credit_card
            )
            dtos.append(dto)

        return dtos

    @staticmethod
    def to_credit_card_model(credit_card: dict) -> CreditCardModel:
        model: CreditCardModel = {
            "exp_date": credit_card.get("exp_date", ""),
            "holder": credit_card.get("holder", ""),
            "number": credit_card.get("number", ""),
            "cvv": credit_card.get("cvv", ""),
            "brand": credit_card.get("brand", ""),
        }

        return model

    @staticmethod
    def to_array_credit_card_model(credit_cards: list[dict]) -> list[CreditCardModel]:
        models = list()

        for credit_card in credit_cards:
            model = CreditCardExtension.to_credit_card_model(credit_card=credit_card)
            models.append(model)

        return models

    @staticmethod
    def to_credit_card_dto(credit_card_model: CreditCardModel) -> CreditCardDto:
        dto: CreditCardDto = {
            "exp_date": credit_card_model["exp_date"],
            "holder": credit_card_model["holder"],
            "number": credit_card_model["number"],
            "cvv": credit_card_model["cvv"],
            "brand": credit_card_model["brand"],
        }

        return dto

    @staticmethod
    def to_new_credit_card_model(credit_card: CreditCardValidator) -> CreditCardModel:
        credit_card_instance = CreditCard(number=credit_card.number)

        model: CreditCardModel = {
            "exp_date": credit_card.exp_date,
            "holder": credit_card.holder,
            "number": credit_card.number,
            "cvv": credit_card.cvv,
            "brand": credit_card_instance.get_brand(),
        }

        return model
