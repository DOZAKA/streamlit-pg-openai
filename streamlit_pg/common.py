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


class RequestApi:
    def __init__(self, method: str, url: str, headers: dict = None, payload: dict = None):
        self.method: str = method
        self.url: str = url
        self.headers: dict = headers
        self.payload: dict = payload

    def send(self) -> dict:
        import requests

        return requests.request(self.method, self.url, headers=self.headers, data=self.payload)
