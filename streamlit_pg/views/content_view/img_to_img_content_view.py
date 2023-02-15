import streamlit
from . import ContentView
from streamlit_pg.modules.openai_manager.openai_manager import OpenAIManager


class ImgToImgContentView(ContentView):
    def __init__(self, st: streamlit, oai_manager: OpenAIManager):
        super().__init__(st, oai_manager)
        self.content: str = None

    def view(self) -> None:
        self.st.header("[Request]")
        uploaded_file = self.st.file_uploader(label='Pick an image to generate image.')

        if not uploaded_file:
            return None

        image_data: any = uploaded_file.getvalue()

        self.st.image(image_data)
        self.st.button('Send Request', on_click=self.on_click)

    def on_click(self) -> None:
        self.st.header("[Response]")
        self.st.json("response")
