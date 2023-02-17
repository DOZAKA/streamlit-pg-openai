# Welcome to Streamlit Playground!

## How to check OpenAI secret key
[Check secret key](https://platform.openai.com/account/api-keys)
## How to check OpenAI organization
[Check organization code](https://platform.openai.com/account/org-settings)
## How to run?

### Build docker image
```python
$ docker build -t streamlit-pg . --build-arg OPEN_AI_ORG=YOUR_ORG_HERE --build-arg OPEN_AI_API_KEY=YOUR_API_KEY_HERE
```
### Run docker image
```python
$ docker run -p 8501:8501 streamlit-pg
```

If you have any questions, checkout official [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
