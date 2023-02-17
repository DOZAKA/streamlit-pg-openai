import streamlit
from abc import *
from streamlit_pg.modules.openai_manager.openai_manager import OpenAIManager


class ContentView(metaclass=ABCMeta):
    def __init__(self, st: streamlit, oai_manager: OpenAIManager = None):
        self.st = st
        self.oai_manager = oai_manager

    def view(self):
        pass

    def on_click(self):
        pass

