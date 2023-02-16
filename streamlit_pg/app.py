import os
import streamlit
from views.main_view import MainView
from modules.openai_manager.openai_manager import OpenAIManager


def main() -> None:
    open_ai_org: str = os.environ["OPEN_AI_ORG"]
    open_ai_api_key: str = os.environ["OPEN_AI_API_KEY"]

    oai_manager: OpenAIManager = OpenAIManager(open_ai_org, open_ai_api_key)

    main_view: MainView = MainView(streamlit, oai_manager)
    main_view.view()


if __name__ == "__main__":
    main()
