import openai


class OpenAIManager:
    
    def __init__(self, org: str = None, api_key: str = None):
        openai.organization = org
        openai.api_key = api_key

    def get_model_list(self) -> list:
        try: 
            return openai.Model.list()
        except Exception as e:
            print(e)
            return None

    # Image Gerneration(https://platform.openai.com/docs/guides/images/usage)
    
    def text_to_image_url(self, text: str, size: str = "1024x1024") -> str:
        datas: list = self.text_to_image_urls(text, 1, size)

        if not datas:
            return None

        data: dict = datas.pop()
    
        return data.get("url", None)

    def text_to_image_urls(self, text: str, n: int = 1, size: str = "1024x1024") -> list:
        try: 
            response: dict = openai.Image.create(
                prompt=text,
                n=n,
                size=size
            )
            return response.get("data", None)
        except Exception as e:
            print(e)
            return None
        
    def image_to_image_url(self, image: any, size: str = "1024x1024") -> str:
        datas: list = self.image_to_image_urls(image, 1, size)

        if not datas:
            return None

        data: dict = datas.pop()
    
        return data.get("url", None)

    def image_to_image_urls(self, image: any, n: int = 1, size: str = "1024x1024") -> list:
        try: 
            response: dict = openai.Image.create_variation(
                image=image,
                n=n,
                size=size
            )

            return response.get("data", None)
        except Exception as e:
            print(e)
            return None

    def moderation(self, content: str) -> list:
        try: 
            response = openai.Moderation.create(
                input=content
            )

            return response.get("results", None)
        except Exception as e:
            print(e)
            return None
