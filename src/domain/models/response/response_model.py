# Standard
import json

# Third Party
from fastapi import Response


class ResponseModel:
    def __init__(self, success: bool, message: str = None, result: dict = None):
        self.__success = success
        self.__message = message
        self.__result = result

    def __build_encoded_content(self) -> str:
        response_dict = {
            "success": self.__success,
            "message": self.__message,
            "result": self.__result,
        }

        encoded_response_dict = json.dumps(response_dict)

        return encoded_response_dict

    def build_http_response(self, status_code: int) -> Response:
        encoded_response_dict = self.__build_encoded_content()

        http_response = Response(content=encoded_response_dict, status_code=status_code)

        return http_response
