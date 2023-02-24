import json
import validators
from . import ContentView
from streamlit_pg.common import RequestApi, HttpRequestMethod, HttpRequestTabs, AuthType


class CustomApiView(ContentView):
    def view(self) -> None:
        self.st.header("[Request]")

        method_col, url_col = self.st.columns(2)
        method: str = method_col.selectbox("HTTP Method", HttpRequestMethod.values())
        url: str = url_col.text_input("URL", "http://")

        auth_type: AuthType = AuthType.NO_AUTH
        auth_info: any = None
        headers: dict = {
            "Content-Type": "application/json"
        }
        payload: dict = dict()

        auth_tab, headers_tab, body_tab = self.st.tabs(HttpRequestTabs.values())

        with auth_tab:
            auth_type = AuthType(auth_tab.selectbox("Auth Type", AuthType.values()))

            if auth_type == AuthType.NO_AUTH:
                auth_info = None
            elif auth_type == AuthType.BEARER_TOKEN:
                auth_token: str = auth_tab.text_input("Token")
                auth_info = "Bearer {}".format(auth_token)
            elif auth_type == AuthType.BASIC_AUTH:
                id_col, pw_col = auth_tab.columns(2)
                auth_id: str = id_col.text_input("Username")
                auth_pw: str = pw_col.text_input("Password")
                auth_info = (auth_id, auth_pw)

        with headers_tab:
            headers_str: str = headers_tab.text_area("Headers", json.dumps(headers))
            if headers_str:
                headers = eval(headers_str)

        with body_tab:
            body_str: str = body_tab.text_area("Body", json.dumps(payload))

            if body_str:
                payload = eval(body_str)

        is_clicked: bool = self.st.button('Send Request')

        if not is_clicked:
            return

        if not validators.url(url):
            return

        # JSON DATA
        self.st.header("[Response]")

        if auth_type == AuthType.BEARER_TOKEN:
            headers["Authorization"] = auth_info

        request_api: RequestApi = RequestApi(auth_info, method, url, headers, payload)
        data: dict = request_api.send()
        print(data)
        self.st.json(data)
