import requests
import csv
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_MAPS_API_KEY")


def get_coordinates(address):
    """
    Function to get coordinates
    """
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"

    parameters = {"address": address, "key": api_key}
    try:
        response = requests.get(base_url, parameters)
        response.raise_for_status()
        data = response.json()

        if data["status"] == "OK":
            location = data["results"][0]["geometry"]["location"]
            latitude = location["lat"]
            longitude = location["lng"]
            return latitude, longitude
        else:
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        print(f"Api Response: {response.text}")
        return None


def generate_coordinates():
    """
    Requests the coordinates foor each address in tehe list.
    """
    rows_list = []

    with open("results_homo.csv", "r", encoding="UTF-8") as adr_file:
        csv_reader = csv.DictReader(adr_file)
        colum_names = csv_reader.fieldnames
        colum_names.extend(["Latitude", "Longitude"])

        for row in csv_reader:
            rows_list.append(row)

    with open("location.csv", "w", newline="", encoding="UTF-8") as loc_file:
        csv_writer = csv.DictWriter(loc_file, fieldnames=colum_names)
        csv_writer.writeheader()

        for row in rows_list:
            address = row["txt address"]
            coordinates = get_coordinates(address)

            if coordinates:
                latitude, longitude = coordinates
                row["Latitude"] = latitude
                row["Longitude"] = longitude
            else:
                print(f"Unable to retrieve coordinates for the address: {address}")
                row["Latitude"] = 0
                row["Longitude"] = 0

            csv_writer.writerow(row)


print("Process complete successfully")


def run():
    generate_coordinates()


if __name__ == "__main__":
    run()
