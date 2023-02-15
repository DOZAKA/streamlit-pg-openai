import streamlit
from . import ContentView
from streamlit_pg.modules.openai_manager.openai_manager import OpenAIManager


class TxtToImgContentView(ContentView):
    def __init__(self, st: streamlit, oai_manager: OpenAIManager):
        super().__init__(st, oai_manager)
        self.content: str = None

    def view(self) -> None:
        self.st.header("[Request]")
        self.content = self.st.text_area("Type a Text to generate image.")
        self.st.button('Send Request', on_click=self.on_click)

    def on_click(self) -> None:
        if not self.content:
            return

        self.st.header("[Response]")
        img_url: str = self.oai_manager.text_to_image_url(self.content)
        self.st.image(img_url)
