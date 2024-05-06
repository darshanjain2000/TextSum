import csv
import logging

from Services.summary_service import SummaryService
summary_service = SummaryService()



def process_csv_in_batches(file_path, batch_size=100):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)

            header = next(reader, None)
            if header is None:
                logging.warning("CSV file has no header row.")

            counter = 0
            batch = []

            for row in reader:
                batch.append(row)
                counter += 1

                if counter % batch_size == 0:
                    process_batch(batch)
                    batch = []

            if batch:
                process_batch(batch)

    except FileNotFoundError:
        logging.error(f"File '{file_path}' not found.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def process_batch(batch):
    batched_summary = summary_service.generate_batch_summary(batch)
    print(batched_summary)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    file = "data.csv"
    batch_size = 100
    process_csv_in_batches(file, batch_size)