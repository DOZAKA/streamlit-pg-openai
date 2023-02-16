import streamlit
from . import ContentView
from streamlit_pg.modules.openai_manager.openai_manager import OpenAIManager


class ModerationContentView(ContentView):
    def __init__(self, st: streamlit, oai_manager: OpenAIManager):
        super().__init__(st, oai_manager)

    def view(self) -> None:
        openai_doc: str = "https://platform.openai.com/docs/guides/moderation/moderation"
        self.st.write("OpenAI API Introduction [link](%s)" % openai_doc)
        self.st.header("[Request]")
        content: str = self.st.text_area("Type a Text to moderation")
        is_clicked: bool = self.st.button('Send Request')

        if not is_clicked:
            return

        self.st.header("[Response]")
        data: dict = self.oai_manager.moderation(content)

        if not data:
            return

        self.st.json(data)

    def on_click(self) -> None:
        pass
