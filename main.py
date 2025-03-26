from model.TokenHoldingSecurityData import TokenHoldingSecurityData

from collections import defaultdict
from utils.csv_utils import read_tokens_from_csv, write_tokens_into_csv
from utils.goplus_utils import append_goplus_data
from utils.scraping_utils import scrape_tokens



def print_token_statistics_from_dicts(rows: list[dict]) -> None:
    # Fields to make statistics of
    fields = [
        "buy_tax",
        "sell_tax",
        "is_honeypot",
        "honeypot_with_same_creator",
        "is_mintable",
        "is_blacklisted",
        "is_anti_whale",
        "hidden_owner",
        "is_open_source",
        "owner_percent",
    ]

    stats = {field: defaultdict(int) for field in fields}

    for row in rows:
        for field in fields:
            value = row.get(field)
            stats[field][value] += 1

    for field, value_counts in stats.items():
        print(f"\n📊 Statistics for '{field}':")
        sorted_counts = sorted(
            value_counts.items(),
            key=lambda x: (x[0] is None, -x[1])
        )
        for value, count in sorted_counts:
            print(f"  {repr(value):>12}: {count} tokens")


if __name__ == "__main__":
    # commented since already saved .csv
    # tokens: list[TokenHoldingSecurityData] = scrape_tokens()
    # append_goplus_data(tokens)
    # write_tokens_into_csv(tokens)
    #
    tokens_dict = read_tokens_from_csv()
    print_token_statistics_from_dicts(tokens_dict)