import anthropic
import os

class ClaudeDAL:
    def __init__(self):
        self.client = anthropic.Anthropic(
            
        )
        self.model = "claude-3-haiku-20240307"
        self.max_token = 4096
        self.temperature = 0
    
    def get_llm_response(self, prompt, system_prompt = None):
        try:
            message_list = [{
                "role":"user",
                "content":[{
                      "type":"text",
                      "text":prompt
                }]
            }]

            if system_prompt:
                message_list.insert(0, {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": system_prompt
                        }
                    ]
                })

            message = self.client.messages.create(
            model = self.model,
            max_tokens = self.max_token,
            temperature = self.temperature,
            messages = message_list
        )
            return message.content[0].text
        except Exception as ex:
            return None
