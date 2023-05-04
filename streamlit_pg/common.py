import requests
import urllib
from enum import Enum


class ExtendedEnum(Enum):

    @classmethod
    def values(cls) -> list:
        return [e.value for e in cls]

    def get_index(self) -> int:
        for idx, val in enumerate(self.values()):
            if self.value == val:
                return idx


class HttpRequestMethod(ExtendedEnum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class HttpRequestTabs(ExtendedEnum):
    PARAMS = "Params"
    AUTH = "Auth"
    HEADERS = "Headers"
    BODY = "Body"


class AuthType(ExtendedEnum):
    NO_AUTH = "No Auth"
    BEARER_TOKEN = "Bearer Token"
    BASIC_AUTH = "Basic Auth"


class RequestApi:
    def __init__(self, auth_info: tuple, method: str, url: str, params: dict = None, headers: dict = None, payload: dict = None):
        self.auth_info: tuple = auth_info
        self.method: str = method
        self.url: str = url
        self.params: dict = params
        self.headers: dict = headers
        self.payload: dict = payload

    def send(self) -> dict:
        try:
            req_url: str = self.url

            if self.params:
                is_and_flag: bool = False
                req_url += "?"

                for key in self.params:
                    val: str = self.params.get(key)

                    if is_and_flag:
                        req_url += "&"
                    else:
                        is_and_flag = True

                    req_url += key
                    req_url += "="
                    req_url += urllib.parse.quote(val)

            print(self.auth_info)
            print(self.method)
            print(req_url)
            print(self.headers)
            print(self.params)
            print(self.payload)

            response: requests.Response = requests.request(self.method, req_url, headers=self.headers, data=self.payload, auth=self.auth_info)
            print(response.status_code)
            print(response.text)

            if response.status_code != 200 and not response.json():
                return

            return response.json()
        except Exception as e:
            print(e)
            return None
