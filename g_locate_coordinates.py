import pandas as pd
import gmplot

# Read data from the CSV file into a DataFrame
df = pd.read_csv("adresses.csv")

# Extract latitude and Lngitude Colums from DataFrame
latitudes = df["latitude"]
longitudes = df["longitude"]

# inicialize  a Google Map Plotter With the inicial cordinates
gmap = gmplot.GoogleMapPlotter(latitudes[0], longitudes[0], 13)

# Google Maps API key to the gmap object
gmap.apikey("AIzaSyD00lfdZEkZrhfEmS6svJkW9yyBQGDvJKY")

# Create a scatter plot on the map with red markers
gmap.scatter(latitudes, longitudes, "#FF0000", size=40, marker=False)

# Generate and save the map as an HTML file
gmap.draw("mapa.html")


def map():
    gmap.open("mapa.html")


if __name__ == "__main__":
    map()
