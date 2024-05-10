import csv
import logging
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
                    # process_batch(batch)
                    batch = []

            if batch:
                # process_batch(batch)
                batches_parts.append(batch)

    except FileNotFoundError:
        logging.error(f"File '{file_path}' not found.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    return batches_parts


def process_batch(batch):
    batched_summary = summary_service.generate_batch_summary(batch)
    print(batched_summary)
    return batched_summary


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


def process_start_approach_2_each_summary_and_combine(input_file, per_batch_size, active_approach):
    batches_parts = process_csv_in_batches(input_file, per_batch_size)
    # for testing taking only first 3 batches
    batches_parts = batches_parts[:3]
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

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    file = "data.csv"
    batch_size = 25
    current_approach = 2
    if current_approach == 1:
        process_start_approach_1_previous_summary_add(file, batch_size, current_approach)
    if current_approach == 2:
        process_start_approach_2_each_summary_and_combine(file, batch_size, current_approach)



