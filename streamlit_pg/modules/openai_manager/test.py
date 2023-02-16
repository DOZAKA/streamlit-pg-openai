import os
from unittest import TestCase, TextTestRunner, TestSuite
from streamlit_pg.modules.openai_manager.openai_manager import OpenAIManager


class TestOpenAIManager(TestCase):
    DEFAULT_ORG: str = os.environ["OPEN_AI_ORG"]
    DEFAULT_API_KEY: str = os.environ["OPEN_AI_API_KEY"]
    
    oai_manager: OpenAIManager = None

    @classmethod
    def setUpClass(cls):
        cls.oai_manager: OpenAIManager = OpenAIManager(cls.DEFAULT_ORG, cls.DEFAULT_API_KEY)

    def test_get_model_list(self):
        model_list: list = self.oai_manager.get_model_list()

        print(model_list)
        self.assertIsNotNone(model_list)

    def test_text_to_image_url(self):
        msg: str = "Future of ChatGPT"
        image_url: str = self.oai_manager.text_to_image_url(msg)

        print(image_url)
        self.assertIsNotNone(image_url)

    def test_image_to_image_urls(self):
        img_path: str = "./image.png"
        image: any = open(img_path, "rb")
        image_url: str = self.oai_manager.image_to_image_urls(image)

        print(image_url)
        self.assertIsNotNone(image_url)

    def test_moderation(self):
        msg: str = "Fuck you donald. I will kill you"
        results: str = self.oai_manager.moderation(msg)

        print(results)
        self.assertIsNotNone(results)
    

def suite():
    suite: TestSuite = TestSuite()

    # Test get_model_list
    #suite.addTest(TestOpenAIManager('test_get_model_list'))
        
    # Test text_to_image_url
    suite.addTest(TestOpenAIManager('test_text_to_image_url'))

    # Test image_to_image_url
    #suite.addTest(TestOpenAIManager('test_image_to_image_urls'))

    # Test Moderation (컨텐츠 조정 시스템)
    #suite.addTest(TestOpenAIManager('test_moderation'))

    return suite

if __name__ == "__main__":
    runner = TextTestRunner(verbosity=2)
    runner.run(suite())
