import streamlit
from .custom_api_view import CustomApiView
from streamlit_pg.common import HttpRequestMethod


class PapagoApiView(CustomApiView):

    def __init__(self, st: streamlit):
        super().__init__(st)

        self.api_description: str = "PAPAGO Translation API"
        self.url: str = "https://openapi.naver.com/v1/papago/n2mt"
        self.method: HttpRequestMethod = HttpRequestMethod.POST
        self.param_info: dict = {
            "source": "ko",
            "target": "en",
            "text": ""
        }
        self.header_info: dict = {
                "Content-Type": "application/json",
                "X-Naver-Client-Id": "",
                "X-Naver-Client-Secret": "",
            }
        self.body_info: dict = {

        }
