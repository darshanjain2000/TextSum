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

    def generate_final_summary_with_quant_data(self, previous_summary, quant_data_summary):
        prompt = self.prompt.generate_final_summary_with_quant_data(previous_summary, quant_data_summary)
        batch_summary = self.llm_client.get_llm_response(prompt)
        return batch_summary


    def generate_quant_data_summary_request(self, quant_data):
        prompt = self.prompt.generate_quant_data_summary_prompt(quant_data)
        batch_summary = self.llm_client.get_llm_response(prompt)
        return batch_summary
