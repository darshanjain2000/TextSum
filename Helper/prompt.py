class Prompt:

    def generate_column_summary(self, active_approach, data_array, previous_summary):
        # verbatim_array = [f"('{entry[0].strip().lower()}', '{entry[1].strip().lower()}')" for entry in data_array]
        prompt = f"""No approach Task Description: You are given a list of feedback comments sourced from a survey for company named Demo Company, where the intent of the survey was get feedback.
                        Your task is to generate a summary of around 100 words for these comments in JSON format.
                        Input: A list of feedback comments and interactions with call center agents, provided as follows:
                        comments = 
                        Output: A JSON object containing the summary of the feedback comments divided into positive and negative along with its key areas and its short explanation, structured as follows:
                        {{
                            "summary": summary gist
                            Positive Area:
                            key area 1 - short explanation
                            key area 2 - short explanation
                            Negative Area:
                            key area 1 - short explanation
                            key area 2 - short explanation
                        }}
                        Requirements:
                        1. Highlight main topics on which management should be focused on.
                        2. Summary Length: The summary should be concise but contain all important points mentioned in the feedback comments.
                        3. Key Points: Ensure that the summary captures key points of the feedback, including positive and negative aspects of the customer experience.
                        4. Clarity: The summary should be clear and understandable to senior members to get an overview of the feedback.
                        5. Contextual Understanding: The LLM should demonstrate an understanding of the context of banking, customer service, and common issues faced by customers.
                        6. Language Style: Use professional and neutral language suitable for presentation to senior members.
                        Additional Notes:
                        - Pay attention to sentiment analysis to distinguish between positive and negative feedback.
                        - Include any specific issues or suggestions mentioned in the comments.
                        - Use natural language generation to create a coherent summary that reflects the general sentiment and concerns of the customers.
                        - Ensure that the summary maintains confidentiality and doesn't disclose personal or sensitive information.
                        - Provide a clear structure to the summary, possibly dividing it into positive and negative aspects for easier understanding.
                        - Avoid redundancy and focus on highlighting unique aspects of the feedback."""
        if active_approach == 1:
            prompt = f"""Task Description: You are given a list of feedback comments sourced from a survey for company named Demo Company, where the intent of the survey was get feedback.
                            Your task is to generate a summary of around 100 words for these comments in JSON format.
                            Input: A list of feedback comments and interactions with call center agents, provided as follows:
                            comments = {data_array}                        
                            Output: A JSON object containing the summary of the feedback comments divided into positive and negative along with its key areas and its short explanation, structured as follows:
                            {{
                                "summary": summary gist
                                Positive Area:
                                key area 1 - short explanation
                                key area 2 - short explanation
                                Negative Area:
                                key area 1 - short explanation
                                key area 2 - short explanation
                            }}
                            Requirements:
                            1. Highlight main topics on which management should be focused on.
                            2. Summary Length: The summary should be concise but contain all important points mentioned in the feedback comments.
                            3. Key Points: Ensure that the summary captures key points of the feedback, including positive and negative aspects of the customer experience.
                            4. Clarity: The summary should be clear and understandable to senior members to get an overview of the feedback.
                            5. Contextual Understanding: The LLM should demonstrate an understanding of the context of banking, customer service, and common issues faced by customers.
                            6. Language Style: Use professional and neutral language suitable for presentation to senior members.
                            Additional Notes:
                            - We have a summary generated from our previous comments = {previous_summary}. Take this also in consideration while generating summary of current comments
                            - Pay attention to sentiment analysis to distinguish between positive and negative feedback.
                            - Include any specific issues or suggestions mentioned in the comments.
                            - Use natural language generation to create a coherent summary that reflects the general sentiment and concerns of the customers.
                            - Ensure that the summary maintains confidentiality and doesn't disclose personal or sensitive information.
                            - Provide a clear structure to the summary, possibly dividing it into positive and negative aspects for easier understanding.
                            - Avoid redundancy and focus on highlighting unique aspects of the feedback."""
        if active_approach == 2:
            # comments_data = ''
            # for data_dict in data_array:
            #     for key in data_dict:
            #         comments_data += f"{key}:{data_dict[key]};"
            #
            #     comments_data += '\n'
            prompt = f"""Task Description: You are given a list of feedback comments sourced from a survey for company named Demo Company, where the intent of the survey was get feedback.
                                    Your task is to generate a summary of around 100 words for these comments in JSON format.
                                    Input: A list of feedback comments and interactions with call center agents, provided as follows:
                                    comments = {data_array}
                                    Output: A JSON object containing the summary of the feedback comments divided into positive and negative along with its key areas and its short explanation, structured as follows:
                                    {{
                                        "summary": summary gist
                                        Positive Area:
                                        key area 1 - short explanation
                                        key area 2 - short explanation
                                        Negative Area:
                                        key area 1 - short explanation
                                        key area 2 - short explanation
                                    }}
                                    Requirements:
                                    1. Highlight main topics on which management should be focused on.
                                    2. Summary Length: The summary should be concise but contain all important points mentioned in the feedback comments.
                                    3. Key Points: Ensure that the summary captures key points of the feedback, including positive and negative aspects of the customer experience.
                                    4. Clarity: The summary should be clear and understandable to senior members to get an overview of the feedback.
                                    5. Contextual Understanding: The LLM should demonstrate an understanding of the context of banking, customer service, and common issues faced by customers.
                                    6. Language Style: Use professional and neutral language suitable for presentation to senior members.
                                    Additional Notes:
                                    - Pay attention to sentiment analysis to distinguish between positive and negative feedback.
                                    - Include any specific issues or suggestions mentioned in the comments.
                                    - Use natural language generation to create a coherent summary that reflects the general sentiment and concerns of the customers.
                                    - Ensure that the summary maintains confidentiality and doesn't disclose personal or sensitive information.
                                    - Provide a clear structure to the summary, possibly dividing it into positive and negative aspects for easier understanding.
                                    - Avoid redundancy and focus on highlighting unique aspects of the feedback."""

        return prompt

    def generate_master_summary(self, active_approach, all_summaries_data):
        prompt = f"""Task Description: You are given a list of summaries from comments sourced from a survey for company named Demo Company, where the intent of the survey was get feedback.
                        Your task is to generate a main summary of around 100 words by using these summaries in JSON format.
                        Input: A list of summaries of feedback comments and interactions with call center agents, provided as follows:
                        list of summaries = {all_summaries_data}
                        Output: A JSON object containing the summary of the feedback comments divided into positive and negative along with its key areas and its short explanation, structured as follows:
                        {{
                            "summary": summary gist
                            Positive Area:
                            key area 1 - short explanation
                            key area 2 - short explanation
                            Negative Area:
                            key area 1 - short explanation
                            key area 2 - short explanation
                        }}
                        Requirements:
                        1. Highlight main topics on which management should be focused on.
                        2. Summary Length: The summary should be concise but contain all important points mentioned in the feedback comments.
                        3. Key Points: Ensure that the summary captures key points of the feedback, including positive and negative aspects of the customer experience.
                        4. Clarity: The summary should be clear and understandable to senior members to get an overview of the feedback.
                        5. Contextual Understanding: The LLM should demonstrate an understanding of the context of banking, customer service, and common issues faced by customers.
                        6. Language Style: Use professional and neutral language suitable for presentation to senior members.
                        Additional Notes:
                        - Pay attention to sentiment analysis to distinguish between positive and negative feedback.
                        - Include any specific issues or suggestions mentioned in the comments.
                        - Use natural language generation to create a coherent summary that reflects the general sentiment and concerns of the customers.
                        - Ensure that the summary maintains confidentiality and doesn't disclose personal or sensitive information.
                        - Provide a clear structure to the summary, possibly dividing it into positive and negative aspects for easier understanding.
                        - Avoid redundancy and focus on highlighting unique aspects of the feedback."""

        return prompt
