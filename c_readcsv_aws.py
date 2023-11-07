import boto3
import csv


def download_s3():
    """
    Create client to access the s3 service .
    Especify the URL of the file in s3 and download the file from s3.
    """
    try:
        s3 = boto3.client(service_name="s3", region_name="sa-east-1")

        adr_url = "s3://techtestsbancol/addresses.csv"
        s3.download_file("techtestsbancol", "addresses.csv", "addresses.csv")

    except Exception as e:
        print(f"Download error: {str(e)}")


def read_adrcsv():
    try:
        addresses_list = []
        with open("addresses.csv", "r", encoding="UTF-8") as adrfile:
            addrreader = csv.reader(adrfile)
            for value in addrreader:
                addresses_list.append(value)
        return addresses_list

    except Exception as e:
        print(f"read error: {str(e)}")


def run():
    download_s3()
    addresses_list = read_adrcsv()
    for line in addresses_list:
        print(line)


if __name__ == "__main__":
    run()
