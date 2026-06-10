import json
from openai import OpenAI


class LLMService:

    def __init__(self):

        self.client = OpenAI(
            api_key="sk-bde88dcbbd5d48eebdaad600e352e114",
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        )

    def chat(self, prompt):

        response = self.client.chat.completions.create(
            model="qwen-max",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.8
        )

        return response.choices[0].message.content