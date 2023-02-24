import json
import streamlit
import validators
from . import ContentView
from streamlit_pg.common import RequestApi, HttpRequestMethod, HttpRequestTabs, AuthType


class CustomApiView(ContentView):
    def __init__(self, st: streamlit):
        super().__init__(st)

        self.st.session_state["RESPONSE_DATA"] = dict()
        self.auth_tab = self.st.empty()
        self.headers_tab = self.st.empty()
        self.body_tab = self.st.empty()
        self.response_area = self.st.empty()

    def view(self) -> None:
        self.st.info("info", icon="ℹ️")
        self.request_view()
        is_clicked = self.send_button_view()
        if is_clicked:
            self.response_view()

    def request_view(self) -> None:
        with self.st.expander("[API Request]", True):
            method_col, url_col = self.st.columns(2)
            method_col.selectbox("HTTP Method", HttpRequestMethod.values(), key="METHOD")
            url_col.text_input("URL", "https://", key="URL")
            self.auth_tab, self.headers_tab, self.body_tab = self.st.tabs(HttpRequestTabs.values())

            self.auth_tab_view()
            self.headers_tab_view()
            self.body_tab_view()

    def send_button_view(self) -> bool:
        _, _, _, _, button_col = self.st.columns(5)
        return button_col.button('Send Request')

    def response_view(self) -> None:
        with self.st.expander("[API Response]"):
            self.st.json(self.st.session_state.RESPONSE_DATA)

    def auth_tab_view(self) -> None:
        with self.auth_tab:
            auth_type: AuthType = AuthType(self.auth_tab.selectbox("Auth Type", AuthType.values()))
            auth_info: any = None
            self.st.session_state["AUTH_TYPE"] = auth_type

            if auth_type == AuthType.BEARER_TOKEN:
                auth_token: str = self.auth_tab.text_input("Token")
                auth_info = "Bearer {}".format(auth_token)
            elif auth_type == AuthType.BASIC_AUTH:
                id_col, pw_col = self.auth_tab.columns(2)
                auth_id: str = id_col.text_input("Username")
                auth_pw: str = pw_col.text_input("Password")
                auth_info = (auth_id, auth_pw)

            self.st.session_state["AUTH_INFO"] = auth_info

    def headers_tab_view(self) -> None:
        with self.headers_tab:
            headers: dict = {
                "Content-Type": "application/json"
            }
            headers_str: str = self.headers_tab.text_area("Headers", json.dumps(headers))
            if headers_str:
                self.st.session_state["HEADERS"] = eval(headers_str)
            else:
                self.st.session_state["HEADERS"] = None

    def body_tab_view(self) -> None:
        with self.body_tab:
            body: str = self.body_tab.text_area("Body", json.dumps({}))

            if body:
                self.st.session_state["BODY"] = eval(body)
            else:
                self.st.session_state["BODY"] = None

    def send_request(self):
        auth_type: AuthType = self.st.session_state.AUTH_TYPE
        auth_info: any = self.st.session_state.AUTH_INFO
        method: str = self.st.session_state.METHOD
        url: str = self.st.session_state.URL
        headers: dict = self.st.session_state.HEADERS
        body: dict = self.st.session_state.BODY

        if not validators.url(url):
            return

        if auth_type == AuthType.BEARER_TOKEN:
            headers["Authorization"] = auth_info

        request_api: RequestApi = RequestApi(auth_info, method, url, headers, body)
        self.st.session_state["RESPONSE_DATA"] = request_api.send()
