import csv
import logging
import random
from time import sleep

from Services.summary_service import SummaryService

summary_service = SummaryService()

def process_csv_in_batches(file_path, batch_size=100):
    batches_parts = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)

            header = next(reader, None)
            if header is None:
                logging.warning("CSV file has no header row.")

            counter = 0
            batch = []

            for row in reader:
                row_dic = {}
                for index, col in enumerate(row):
                    row_dic[header[index]] = col

                batch.append(row_dic)
                counter += 1

                if counter % batch_size == 0:
                    batches_parts.append(batch)
                    batch = []

            if batch:
                batches_parts.append(batch)

    except FileNotFoundError:
        logging.error(f"File '{file_path}' not found.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    return batches_parts

def process_csv_with_random_data(file_path, batch_size=100):
    batches = []
    promoters = []
    passive = []
    detractor = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)

            header = next(reader, None)
            if header is None:
                logging.warning("CSV file has no header row.")

            counter = 0
            batch = []

            for row in reader:
                row_dic = {}
                for index, col in enumerate(row):
                    row_dic[header[index]] = col

                batch.append(row_dic)
                if (row[3] == 'Promoters'):
                    promoters.append(row_dic)
                if (row[3] == 'Passive'):
                    passive.append(row_dic)
                if (row[3] == 'Detractor'):
                    detractor.append(row_dic)

                counter += 1

        each_batch_size = round(batch_size/3)
        selected_promoters = random.sample(promoters, each_batch_size)
        selected_passive = random.sample(passive, each_batch_size)
        selected_detractor = random.sample(detractor, each_batch_size)
        batches.extend(selected_promoters)
        batches.extend(selected_passive)
        batches.extend(selected_detractor)

    except FileNotFoundError:
        logging.error(f"File '{file_path}' not found.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    return batches


def process_start_approach_1_previous_summary_add(input_file, per_batch_size, active_approach):
    batches_parts = process_csv_in_batches(input_file, per_batch_size)
    # for testing taking only first 3 batches
    # batches_parts = batches_parts[:3]
    print(len(batches_parts))
    current_batch = 0
    current_batch_summary = ''
    while current_batch < len(batches_parts):
        print(current_batch)
        current_batch_summary = summary_service.generate_batch_summary(active_approach, batches_parts[current_batch],
                                                                       current_batch_summary)
        print(f"batch: {current_batch}, summary: {current_batch_summary}")
        sleep_secs = 10
        print(f"sleeping for {sleep_secs} seconds")
        sleep(sleep_secs)
        current_batch = current_batch + 1

    print(f"completed {current_batch_summary}")
    return current_batch_summary


def process_start_approach_2_each_summary_and_combine(input_file, per_batch_size, active_approach):
    batches_parts = process_csv_in_batches(input_file, per_batch_size)
    # for testing taking only first 3 batches
    # batches_parts = batches_parts[:1]
    print(len(batches_parts))
    current_batch = 0
    batches_summaries = []
    while current_batch < len(batches_parts):
        print(current_batch)
        current_batch_summary = summary_service.generate_batch_summary(active_approach, batches_parts[current_batch], '')
        print(f"batch: {current_batch}, summary: {current_batch_summary}")
        batches_summaries.append(current_batch_summary)
        sleep_secs = 15
        print(f"sleeping for {sleep_secs} seconds")
        sleep(sleep_secs)
        current_batch = current_batch + 1

    print(f"All batches summary {batches_summaries}")
    main_summary = summary_service.generate_master_summary(active_approach, batches_summaries)
    print(f"Master summary below>>>>")
    print(f"{main_summary}")
    return main_summary

def process_start_approach_2_each_summary_and_combine_with_approach_a_send_quant_data_summary_along_with_questions(input_file, per_batch_size, active_approach):
    quant_data_summary = generate_quant_data_summary()


    batches_parts = process_csv_in_batches(input_file, per_batch_size)
    # for testing taking only first 3 batches
    # batches_parts = batches_parts[:1]
    print(len(batches_parts))
    current_batch = 0
    batches_summaries = []
    while current_batch < len(batches_parts):
        print(current_batch)
        current_batch_summary = summary_service.generate_batch_summary(active_approach, batches_parts[current_batch], '')
        print(f"batch: {current_batch}, summary: {current_batch_summary}")
        batches_summaries.append(current_batch_summary)
        sleep_secs = 10
        print(f"sleeping for {sleep_secs} seconds")
        sleep(sleep_secs)
        current_batch = current_batch + 1

    print(f"All batches summary {batches_summaries}")
    main_summary = summary_service.generate_master_summary(active_approach, batches_summaries)
    print(f"Master summary below>>>>")
    print(f"{main_summary}")
    return main_summary

def process_start_approach_3_take_random_data(input_file, batch_size, active_approach):
    batches_parts = process_csv_with_random_data(input_file, batch_size)
    main_summary = summary_service.generate_batch_summary(active_approach, batches_parts, '')
    print(f"Master summary below>>>>")
    print(f"{main_summary}")
    return main_summary

def add_quantitative_data_summary(previous_summary, quant_data_summary):
    final_summary = summary_service.generate_final_summary_with_quant_data(previous_summary, quant_data_summary)
    return final_summary

def get_quant_data_from_csv(file_path):
    quant_data = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                quant_data.append(row)

    except FileNotFoundError:
        logging.error(f"File '{file_path}' not found.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    return quant_data

def generate_quant_data_summary():
    file_path = "input_data_survey_telesales/numeric_data_survey_flexi_telesales.csv"
    quant_data = get_quant_data_from_csv(file_path)
    main_summary = summary_service.generate_quant_data_summary_request(quant_data)
    return main_summary

def generate_quant_data_summary_along_with_questions_and_key_metrics():
    file_path = "input_data_survey_telesales/numeric_data_survey_flexi_telesales.csv"
    quant_data = get_quant_data_from_csv(file_path)
    main_summary = summary_service.generate_quant_data_summary_request(quant_data)
    return main_summary


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    final_summary = ''
    file = "input_data_survey_telesales/survey-telesales.csv"
    batch_size = 30
    current_approach = 2
    if current_approach == 1:
        final_summary = process_start_approach_1_previous_summary_add(file, batch_size, current_approach)
    if current_approach == 2:
        final_summary = process_start_approach_2_each_summary_and_combine(file, batch_size, current_approach)
    if current_approach == 21:
        final_summary = process_start_approach_2_each_summary_and_combine_with_approach_a_send_quant_data_summary_along_with_questions(file, batch_size, current_approach)
    if current_approach == 3:
        final_summary = process_start_approach_3_take_random_data(file, batch_size, current_approach)

    quant_data_summary = generate_quant_data_summary()
    summary_with_quant_data = add_quantitative_data_summary(final_summary, quant_data_summary)

    print(f"Final summary with quant data below>>>>")
    print(f"{summary_with_quant_data}")

