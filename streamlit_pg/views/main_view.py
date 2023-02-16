import streamlit
from enum import Enum
from .content_view import ContentView
from .content_view.image_generations_content_view import ImageGenerationsView
from .content_view.image_variations_view import ImageVariationsView
from .content_view.moderation_content_view import ModerationContentView
from streamlit_pg.modules.openai_manager.openai_manager import OpenAIManager


class ExtendedEnum(Enum):

    @classmethod
    def values(cls) -> tuple:
        return (e.value for e in cls)


class ModelType(ExtendedEnum):
    IMAGE_GENERATIONS = "IMAGE_GENERATIONS"
    IMAGE_VARIATIONS = "IMAGE_VARIATIONS"
    TEXT_MODERATION = "TEXT_MODERATION"


class MainView:
    def __init__(self, st: streamlit, oai_manager: OpenAIManager):
        self.st = st
        self.oai_manager: OpenAIManager = oai_manager
        self.selected_type: ModelType = ModelType.IMAGE_GENERATIONS
        self.content_view: ContentView = None

    def view(self):
        self.st.sidebar.header("Streamlit Playground for OpenAI")
        selected_type: ModelType = ModelType(self.st.sidebar.selectbox("Select Test Model Type.", ModelType.values()))

        if selected_type == ModelType.IMAGE_GENERATIONS:
            self.content_view = ImageGenerationsView(self.st, self.oai_manager)
        elif selected_type == ModelType.IMAGE_VARIATIONS:
            self.content_view = ImageVariationsView(self.st, self.oai_manager)
        elif selected_type == ModelType.TEXT_MODERATION:
            self.content_view = ModerationContentView(self.st, self.oai_manager)

        self.content_view.view()
