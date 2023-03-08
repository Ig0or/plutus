# Standard
from datetime import date
from typing import Optional, NoReturn

# Third Party
from creditcard import CreditCard
from pydantic import BaseModel, validator


class CreditCardValidator(BaseModel):
    exp_date: str
    holder: str
    number: str
    cvv: Optional[str]

    @staticmethod
    def __check_date_contains_slash(exp_date: str) -> tuple[str, str]:
        if "/" not in exp_date[2] or exp_date.count("/") > 1:
            raise ValueError("The exp date must follow the format MM/YYYY.")

        month, year = exp_date.split(sep="/")

        return month, year

    @staticmethod
    def __check_date_length(month: str, year: str) -> NoReturn:
        if len(month) != 2 or len(year) != 4:
            raise ValueError("The exp date must follow the format MM/YYYY.")

        return

    @staticmethod
    def __check_date_numeric(month: str, year: str) -> NoReturn:
        if not month.isnumeric() or not year.isnumeric():
            raise ValueError(
                "The MM and YYYY values must be numerics and follow the format MM/YYYY."
            )

        return

    @staticmethod
    def __check_valid_month(month: str) -> NoReturn:
        valid_months = [
            "01",
            "02",
            "03",
            "04",
            "05",
            "06",
            "07",
            "08",
            "09",
            "10",
            "11",
            "12",
        ]

        if month not in valid_months:
            raise ValueError("The MM value from exp date must be between 01 and 12")

        return

    @staticmethod
    def __check_date_is_not_expired(expiry_month: str, expiry_year: str) -> NoReturn:
        actual_date = date.today()
        actual_month = actual_date.month
        actual_year = actual_date.year

        if actual_year > int(expiry_year):
            raise ValueError("The exp date is already expired.")

        if actual_month > int(expiry_month) and actual_year >= int(expiry_year):
            raise ValueError("The exp date is already expired.")

        return

    @validator("exp_date")
    def validate_exp_date(cls, exp_date: str) -> str:
        month, year = cls.__check_date_contains_slash(exp_date=exp_date)

        cls.__check_date_length(month=month, year=year)
        cls.__check_date_numeric(month=month, year=year)
        cls.__check_valid_month(month=month)
        cls.__check_date_is_not_expired(expiry_month=month, expiry_year=year)

        return exp_date

    @validator("holder")
    def validate_holder(cls, holder: str) -> str:
        if len(holder) <= 2:
            raise ValueError("The holder name must be more than two characters.")

        return holder

    @validator("number")
    def validate_number(cls, number: str) -> str:
        credit_card = CreditCard(number=number)

        if not credit_card.is_valid():
            raise ValueError("The number is invalid.")

        return number

    @staticmethod
    def __check_cvv_null(cvv: str) -> NoReturn:
        if not cvv:
            raise ValueError("The cvv can't be a null value.")

        return

    @staticmethod
    def __check_cvv_length(cvv: str) -> NoReturn:
        if len(cvv) < 3 or len(cvv) > 4:
            raise ValueError(
                "The cvv must be more than three characters and less than four characters."
            )

        return

    @staticmethod
    def __check_cvv_numeric(cvv: str) -> NoReturn:
        if not cvv.isnumeric():
            raise ValueError("The cvv must be numeric.")

        return

    @validator("cvv")
    def validate_cvv(cls, cvv: str) -> str:
        cls.__check_cvv_null(cvv=cvv)
        cls.__check_cvv_length(cvv=cvv)
        cls.__check_cvv_numeric(cvv=cvv)

        return cvv
