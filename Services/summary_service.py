from DALs.claudeDAL import ClaudeDAL
from Helper.prompt import Prompt


class SummaryService:
    def __init__(self):
        self.llm_client = ClaudeDAL()
        self.prompt = Prompt()

    def generate_batch_summary(self, active_approach, rows_data, previous_summary):
        prompt = self.prompt.generate_column_summary(active_approach, rows_data, previous_summary)
        batch_summary = self.llm_client.get_llm_response(prompt)

        return batch_summary

    def generate_master_summary(self, active_approach, all_summaries_data):
        prompt = self.prompt.generate_master_summary(active_approach, all_summaries_data)
        batch_summary = self.llm_client.get_llm_response(prompt)

        return batch_summary
