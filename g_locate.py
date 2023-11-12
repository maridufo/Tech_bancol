import pandas as pd
import gmplot
import os
from dotenv import load_dotenv
import webbrowser


def generate_map():
    df = pd.read_csv("location.csv")

    # Extract latitude and Lngitude Colums from DataFrame
    latitudes = df["Latitude"]
    longitudes = df["Longitude"]

    # inicialize  a Google Map Plotter With the inicial cordinates
    gmap = gmplot.GoogleMapPlotter(latitudes.iloc[0], longitudes.iloc[0], 13)

    # Google Maps API key to the gmap object
    load_dotenv()
    google_maps_api_key = os.getenv("google_maps_api_key")
    gmap.apikey = google_maps_api_key

    # Create a scatter plot on the map with red markers
    for index, row in df.iterrows():
        latitude = float(row["Latitude"])
        longitude = float(row["Longitude"])

        if latitude != 0:
            gmap.marker(latitude, longitude, "#FF0000", tittle=row["txt address"])

    # Generate and save the map as an HTML file
    gmap.draw("mapa.html")

    def show_map():
        webbrowser.open("mapa.html")

    if __name__ == "__main__":
        show_map()


def run():
    generate_map()


if __name__ == "__main__":
    run()
