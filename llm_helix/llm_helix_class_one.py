class llm_helix:
    def __init__(self):
        self.messages = []
        self.client_messages = []
        self.lead_model = "gpt-4o-mini"
        self.functions_called = []
        