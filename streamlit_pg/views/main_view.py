import streamlit
from enum import Enum
from .content_view import ContentView
from .content_view.txt_to_img_content_view import TxtToImgContentView
from .content_view.img_to_img_content_view import ImgToImgContentView
from .content_view.moderation_content_view import ModerationContentView
from streamlit_pg.modules.openai_manager.openai_manager import OpenAIManager


class ExtendedEnum(Enum):

    @classmethod
    def values(cls) -> tuple:
        return (e.value for e in cls)


class ModelType(ExtendedEnum):
    TEXT_TO_IMAGE = "TEXT_TO_IMAGE"
    IMAGE_TO_IMAGE = "IMAGE_TO_IMAGE"
    MODERATION = "MODERATION"


class MainView:
    def __init__(self, st: streamlit, oai_manager: OpenAIManager):
        self.st = st
        self.oai_manager: OpenAIManager = oai_manager
        self.selected_type: ModelType = ModelType.TEXT_TO_IMAGE
        self.content_view: ContentView = None

    def view(self):
        self.st.sidebar.header("Streamlit Playground for OpenAI")
        selected_type: ModelType = ModelType(self.st.sidebar.selectbox("Select Test Model Type.", ModelType.values()))

        if selected_type == ModelType.TEXT_TO_IMAGE:
            self.content_view = TxtToImgContentView(self.st, self.oai_manager)
        elif selected_type == ModelType.IMAGE_TO_IMAGE:
            self.content_view = ImgToImgContentView(self.st, self.oai_manager)
        elif selected_type == ModelType.MODERATION:
            self.content_view = ModerationContentView(self.st, self.oai_manager)

        self.content_view.view()
