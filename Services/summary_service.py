from DALs.claudeDAL import ClaudeDAL
from Helper.prompt import Prompt


class SummaryService():
    def __init__(self):
        self.llm_client = ClaudeDAL()

    def generate_batch_summary(self, rows_data):
        prompt = Prompt().generate_column_summary(rows_data)
        batch_summary = self.llm_client.get_llm_response(prompt)

        return batch_summary