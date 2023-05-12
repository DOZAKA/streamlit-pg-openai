import json
import streamlit
import validators
from . import ContentView
from streamlit_pg.common import RequestApi, HttpRequestMethod, HttpRequestTabs, AuthType


class CustomApiView(ContentView):
    def __init__(self, st: streamlit):
        super().__init__(st)

        self.st.session_state["RESPONSE_DATA"] = dict()

        self.api_description: str = "Custom API"
        self.url: str = "https://"
        self.method: HttpRequestMethod = HttpRequestMethod.GET
        self.param_info: dict = {}
        self.header_info: dict = {
            "Content-Type": "application/json"
        }
        self.body_info: dict = {}

    def view(self) -> None:
        self.st.info(self.api_description, icon="ℹ️")
        self.request_view()

    def request_view(self) -> None:
        with self.st.expander("[API Request]", True):
            method_col, url_col = self.st.columns(2)
            method_col.selectbox("HTTP Method", HttpRequestMethod.values(), index=self.method.get_index(), key="METHOD")
            url_col.text_input("URL", self.url, key="URL")
            params_tab, auth_tab, headers_tab, body_tab = self.st.tabs(HttpRequestTabs.values())

            with params_tab:
                self.params_tab_view()

            with auth_tab:
                self.auth_tab_view()

            with headers_tab:
                self.headers_tab_view()

            with body_tab:
                self.body_tab_view()

        _, _, _, _, button_col = self.st.columns(5)

        if button_col.button("Send Request"):
            self.send_request()

    def params_tab_view(self) -> None:
        tmp_param_info: dict = dict()

        default_param_cnt: int = len(self.param_info)
        default_param_keys: list = list(self.param_info)
        param_cnt: int = self.st.number_input("Param Count", value=default_param_cnt, max_value=20, min_value=0)

        for i in range(param_cnt):
            default_key: str = ""
            default_val: str = ""

            if default_param_keys:
                default_key = default_param_keys.pop(0)
                default_val = self.param_info.get(default_key)

            key_col, val_col = self.st.columns(2)

            k: str = key_col.text_input("KEY", key="PARAM_KEY" + str(i), value=default_key)
            v: str = val_col.text_input("VALUE", key="PARAM_VALUE" + str(i), value=default_val)

            tmp_param_info[k] = v

        self.st.session_state["PARAMS"] = tmp_param_info

    def auth_tab_view(self) -> None:
        auth_type: AuthType = AuthType(self.st.selectbox("Auth Type", AuthType.values()))
        auth_info: any = None
        self.st.session_state["AUTH_TYPE"] = auth_type

        if auth_type == AuthType.BEARER_TOKEN:
            auth_token: str = self.st.text_input("Token")
            auth_info = "Bearer {}".format(auth_token)
        elif auth_type == AuthType.BASIC_AUTH:
            id_col, pw_col = self.st.columns(2)
            auth_id: str = id_col.text_input("Username")
            auth_pw: str = pw_col.text_input("Password")
            auth_info = (auth_id, auth_pw)

        self.st.session_state["AUTH_INFO"] = auth_info

    def headers_tab_view(self) -> None:
        tmp_header_info: dict = dict()

        default_header_cnt: int = len(self.header_info)
        default_header_keys: list = list(self.header_info)
        header_cnt: int = self.st.number_input("Header Count", value=default_header_cnt, max_value=20, min_value=0)

        for i in range(header_cnt):
            default_key: str = ""
            default_val: str = ""

            if default_header_keys:
                default_key = default_header_keys.pop(0)
                default_val = self.header_info.get(default_key)

            key_col, val_col = self.st.columns(2)

            k: str = key_col.text_input("KEY", key="HEADER_KEY" + str(i), value=default_key)
            v: str = val_col.text_input("VALUE", key="HEADER_VALUE" + str(i), value=default_val)

            tmp_header_info[k] = v

        self.st.session_state["HEADERS"] = tmp_header_info

    def body_tab_view(self) -> None:
        body: str = self.st.text_area("Body", json.dumps(self.body_info))

        if body:
            self.st.session_state["BODY"] = eval(body)
        else:
            self.st.session_state["BODY"] = None

    def response_view(self) -> None:
        with self.st.expander("[API Response]", True):
            self.st.json(self.st.session_state.RESPONSE_DATA)

    def send_request(self) -> dict:
        auth_type: AuthType = self.st.session_state.AUTH_TYPE
        auth_info: any = self.st.session_state.AUTH_INFO
        method: str = self.st.session_state.METHOD
        url: str = self.st.session_state.URL
        params: dict = self.st.session_state.PARAMS
        headers: dict = self.st.session_state.HEADERS
        body: dict = self.st.session_state.BODY

        if not validators.url(url):
            return

        if auth_type == AuthType.BEARER_TOKEN:
            headers["Authorization"] = auth_info

        request_api: RequestApi = RequestApi(auth_info, method, url, params, headers, body)

        self.st.session_state["RESPONSE_DATA"] = request_api.send()
        self.response_view()
