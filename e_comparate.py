import csv
from fuzzywuzzy import fuzz


def read_file_txt(addresses_h):
    with open(addresses_h, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


def read_file_csv(addresses):
    with open(addresses, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row["address"] for row in reader]


def addresses_compare(txt_addresses, csv_addresses, threshold=90):
    results = []
    for txt_addresses in txt_addresses:
        best_match = max(csv_addresses, key=lambda x: fuzz.ratio(txt_addresses, x))
        match_percent = fuzz.ratio(txt_addresses, best_match)
        if match_percent >= threshold and txt_addresses != best_match:
            results.append({"txt address": txt_addresses, "match": f"{match_percent}%"})
    return results


def results_hom():
    txt_file = "addresses_h.txt"
    csv_file = "addresses.csv"

    txt_addresses = read_file_txt(txt_file)
    csv_addresses = read_file_csv(csv_file)

    results = addresses_compare(txt_addresses, csv_addresses)

    with open("results_homo.csv", "w", encoding="utf-8") as output_file:
        fieldnames = ["txt address", "match"]
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)

        writer.writeheader()
        for result in results:
            writer.writerow(result)

    print("results save in results_homo.txt)")


def run():
    results_hom()


if __name__ == "__main__":
    run()
