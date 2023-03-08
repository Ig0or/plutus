# Standard
from typing import NoReturn

# Local
from src.domain.dtos.credit_card.resumed_credit_card_dto import ResumedCreditCardDto
from src.domain.exceptions.exceptions import CreditCardAlreadyExists
from src.domain.extensions.credit_card.credit_card_extension import CreditCardExtension
from src.domain.models.credit_card.credit_card_model import CreditCardModel
from src.domain.validators.credit_card.credit_card_validator import CreditCardValidator
from src.repositories.credit_card.credit_card_repository import CreditCardRepository
from src.services.obfuscate_data.obfuscate_data_service import ObfuscateDataService


class CreditCardService:
    @staticmethod
    def __decrypt_credit_cards_number(
        credit_cards: list[CreditCardModel],
    ) -> list[CreditCardModel]:
        decrypted_credit_cards = list()

        for credit_card in credit_cards:
            decrypted_credit_card_number = ObfuscateDataService.deobfuscate_value(
                value=credit_card["number"]
            )

            credit_card["number"] = decrypted_credit_card_number

            decrypted_credit_cards.append(credit_card)

        return decrypted_credit_cards

    @staticmethod
    async def list_credit_cards() -> list[ResumedCreditCardDto]:
        credit_cards_list = await CreditCardRepository.get_all_credit_cards()

        credit_cards_model = CreditCardExtension.to_array_credit_card_model(
            credit_cards=credit_cards_list
        )

        decrypted_credit_cards = CreditCardService.__decrypt_credit_cards_number(
            credit_cards=credit_cards_model
        )

        resumed_credit_cards_dto = CreditCardExtension.to_array_resumed_credit_card_dto(
            credit_cards_model=decrypted_credit_cards
        )

        return resumed_credit_cards_dto

    @staticmethod
    def __encrypt_credit_card_number(credit_card_number: str) -> str:
        encrypted_credit_card_number = ObfuscateDataService.obfuscate_value(
            value=credit_card_number
        )

        return encrypted_credit_card_number

    @staticmethod
    async def __verify_credit_card_already_exists(credit_card_number: str) -> NoReturn:
        credit_cards = await CreditCardRepository.get_all_credit_cards()

        decrypted_credit_cards = CreditCardService.__decrypt_credit_cards_number(
            credit_cards=credit_cards
        )

        for credit_card in decrypted_credit_cards:
            if credit_card["number"] == credit_card_number:
                raise CreditCardAlreadyExists()

        return

    @staticmethod
    async def create_credit_card(credit_card: CreditCardValidator) -> NoReturn:
        credit_card_model = CreditCardExtension.to_new_credit_card_model(
            credit_card=credit_card
        )

        await CreditCardService.__verify_credit_card_already_exists(
            credit_card_number=credit_card_model["number"]
        )

        encrypted_credit_card_number = CreditCardService.__encrypt_credit_card_number(
            credit_card_number=credit_card_model["number"]
        )

        credit_card_model["number"] = encrypted_credit_card_number

        await CreditCardRepository.save_new_credit_card(
            credit_card_model=credit_card_model
        )

        return
