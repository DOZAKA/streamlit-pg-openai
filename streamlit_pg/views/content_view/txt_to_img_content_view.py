import streamlit
from . import ContentView
from streamlit_pg.modules.openai_manager.openai_manager import OpenAIManager


class TxtToImgContentView(ContentView):
    def __init__(self, st: streamlit, oai_manager: OpenAIManager):
        super().__init__(st, oai_manager)

    def view(self) -> None:
        openai_doc: str = "https://platform.openai.com/docs/guides/images/generations"
        self.st.write("OpenAI API Introduction [link](%s)" % openai_doc)
        self.st.header("[Request]")
        content: str = self.st.text_area("Type a Text to generate image")
        is_clicked: bool = self.st.button('Send Request')

        if not is_clicked:
            return

        self.st.header("[Response]")
        img_url: str = self.oai_manager.text_to_image_url(content)

        if not img_url:
            return

        self.st.image(img_url)

    def on_click(self) -> None:
        pass

