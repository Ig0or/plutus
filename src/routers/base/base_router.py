# Third Party
from fastapi import FastAPI

# Standard
from typing_extensions import NoReturn

# Local
from src.routers.credit_card.credit_card_router import CreditCardRouter


class BaseRouter:
    __app = FastAPI()

    @classmethod
    def __register_credit_card_routers(cls) -> NoReturn:
        credit_card_routers = CreditCardRouter.get_routers()

        cls.__app.include_router(router=credit_card_routers)

    @classmethod
    def register_routers(cls):
        cls.__register_credit_card_routers()

        return cls.__app
