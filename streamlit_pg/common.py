import requests
from enum import Enum


class ExtendedEnum(Enum):

    @classmethod
    def values(cls) -> list:
        return [e.value for e in cls]


class HttpRequestMethod(ExtendedEnum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class HttpRequestTabs(ExtendedEnum):
    AUTH = "Auth"
    HEADERS = "Headers"
    BODY = "Body"


class AuthType(ExtendedEnum):
    NO_AUTH = "No Auth"
    BEARER_TOKEN = "Bearer Token"
    BASIC_AUTH = "Basic Auth"


class RequestApi:
    def __init__(self, auth_info: tuple, method: str, url: str, headers: dict = None, payload: dict = None):
        self.auth_info: tuple = auth_info
        self.method: str = method
        self.url: str = url
        self.headers: dict = headers
        self.payload: dict = payload
        print(self.auth_info)
        print(self.method)
        print(self.url)
        print(self.headers)
        print(self.payload)

    def send(self) -> dict:
        try:
            response: requests.Response = requests.request(self.method, self.url, headers=self.headers, data=self.payload, auth=self.auth_info)
            print(response.status_code)
            print(response.text)

            if response.status_code != 200:
                return

            return response.json()
        except Exception as e:
            print(e)
            return None
