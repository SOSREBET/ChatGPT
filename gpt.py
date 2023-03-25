import openai
from config import API_GPT


class ChatGPT:
    def __init__(self, model: str="gpt-3.5-turbo"):
        openai.api_key = API_GPT
        self.model = model
        self.messages = list()

    async def ask_question(self, message: str) -> dict:
        self.messages.append({"role": "user", "content": message})
        complemation = await openai.ChatCompletion.acreate(model=self.model, messages=self.messages)
        self.messages.append({"role": "assistant", "content": complemation["choices"][0]["message"].content})
        return complemation.choices[0].message
