from openai import OpenAI
import json
import os
from dotenv import load_dotenv

class llm_helix:
    def __init__(self):
        self.messages = [{"role": "system", "content": "You are a friendly assistant, who always ties back conversations to the Scotty Labs student organization at Carnegie Mellon University."}]
        self.client_messages = []
        self.lead_model = "gpt-4o-mini"
        self.functions_called = []

    def generic_chat(user_query, self):
        load_dotenv()
        client = OpenAI()

        self.messages.append({"role": "user", "content": str(user_query)})
        self.client_messages.append({"role": "user", "content": str(user_query)})

        response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages = self.messages,
        )

        self.messages.append({"role": "assistant", "content": str(response.choices[0].message)})
        self.client_messages.append({"role": "assistant", "content": str(response.choices[0].message)})

        return self.client_messages
