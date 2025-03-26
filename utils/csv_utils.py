import csv
from dataclasses import asdict
from model.TokenHoldingSecurityData import TokenHoldingSecurityData

csv_file_path = "token_security_data_2.csv"

def write_tokens_into_csv(tokens: list[TokenHoldingSecurityData]):
    # Write to CSV
    with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=asdict(tokens[0]).keys())
        writer.writeheader()
        for token in tokens:
            writer.writerow(asdict(token))

def read_tokens_from_csv() -> list[dict]:
    tokens_dict = []

    with open(csv_file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            tokens_dict.append(row)

    # return tokens
    return tokens_dict