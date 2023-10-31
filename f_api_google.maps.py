import requests 
import csv

api_key = "AIzaSyD00lfdZEkZrhfEmS6svJkW9yyBQGDvJKY" #Remember that this account is free and limited

addresses= ["1600 Amphitheatre Parkway","calle 53 # 55 a 67"]

def get_coordinates (address):
    """
    Function to get coordinates
    """
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"

    parameters = {
        "address" : address,
        "key" : api_key
        }
    response = requests.get( base_url, parameters)
    data = response.json()

    if data["status"] =="OK":
        location = data["results"] [0]["geometry"] ["location"]
        latitude = location["lat"]
        longitude = location["lng"]
        return latitude, longitude
    else:
        return None

# Requests the coordinates foor each address in tehe list. 
with open("addresses.csv", "w", encoding="UTF-8") as adrfile:
        for address in addresses:
           coordinates = get_coordinates(address)
           if coordinates:
               latitude, longitude =coordinates
               adrfile.write(F"address: {address}")
               adrfile.write(f"latitude: {latitude}")
               adrfile.write(f"longitude : {longitude}")
        else:
                print(f"Unable to retriev coordinates for the address: {address}")