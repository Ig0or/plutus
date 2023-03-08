# Standard
from typing_extensions import NotRequired, TypedDict


class AbstractResponseDto(TypedDict):
    result: NotRequired[dict | list[dict]]
    message: NotRequired[str]
    success: bool
    status_code: int
