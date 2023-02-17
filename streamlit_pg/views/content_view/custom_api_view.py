import json
from . import ContentView
from streamlit_pg.common import RequestApi, HttpRequestMethod


class CustomApiView(ContentView):
    def view(self) -> None:
        self.st.header("[Request]")

        tmp_headers: str = json.dumps({
            "Content-Type": "application/json"
        })

        method: str = self.st.selectbox("HTTP Method", HttpRequestMethod.values())
        url: str = self.st.text_input("URL", "http://")
        headers: str = self.st.text_area("Header (Type a header to request api)", value=tmp_headers)
        payload: str = self.st.text_area("Payload (Type a payload to request api)")

        is_clicked: bool = self.st.button('Send Request')

        if not is_clicked:
            return

        # JSON DATA
        self.st.header("[Response]")

        json_headers: dict = None if not headers else json.loads(headers.replace("'", "\""))

        request_api: RequestApi = RequestApi(method, url, json_headers, payload)
        data: dict = request_api.send()
        self.st.json(data)
