# Standard
import json

# Third Party
from fastapi import Response


class ResponseDto:
    def __init__(
        self,
        success: bool,
        status_code: int,
        message: str = None,
        result: dict = None,
    ):
        self.__success = success
        self.__status_code = status_code
        self.__message = message
        self.__result = result

    def __build_encoded_content(self) -> str:
        response_dict = {
            "success": self.__success,
            "status_code": self.__status_code,
            "message": self.__message,
            "result": self.__result,
        }

        encoded_response_dict = json.dumps(response_dict)

        return encoded_response_dict

    def build_http_response(self) -> Response:
        encoded_response_dict = self.__build_encoded_content()

        http_response = Response(
            content=encoded_response_dict,
            status_code=self.__status_code,
            media_type="application/json",
        )

        return http_response
