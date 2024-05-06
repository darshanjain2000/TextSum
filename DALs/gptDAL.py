from openai import OpenAI
import os

class GptDAL:
    def __init__(self):
        self.client = OpenAI(
            api_key= os.getenv("GPT_KEY"),
        )
        self.model = "gpt-3.5-turbo-0125"
        self.max_token = 4096
        self.temperature = 0
    
    def get_llm_response(self, prompt, system_prompt = None):
        try:
            message_list = [{
                "role":"user",
                "content":[{
                      "text":prompt
                }]
            }]

            if system_prompt:
                message_list.insert(0, {
                    "role": "system",
                    "content": [
                        {
                            "text": system_prompt
                        }
                    ]
                })

            gpt_response = self.client.chat.completions.create(
            model = self.model,
            max_tokens = self.max_token,
            temperature = self.temperature,
            messages = message_list
        )
            return gpt_response.choices[0].message
        except Exception as ex:
            return None
