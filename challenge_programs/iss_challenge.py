#!/usr/bin/env python3

import requests
import datetime
import reverse_geocoder as rg

API_URL = "http://api.open-notify.org/iss-now.json"

def main(): 
    response = requests.get(API_URL).json()

    print(type(response))
    print(response)
    print("Current Location of the ISS:")
    position = response.get("iss_position")
    print(position)
    lon = position["longitude"]
    lat = position["latitude"]
    coords = (lat, lon)
    location = rg.search(coords)
    city = location[0]["name"]
    country = location[0]["cc"]
    curr_time = response.get("timestamp")
    curr_dt = datetime.datetime.fromtimestamp(curr_time)
    print(f'Timestamp: {curr_dt}')
    print(f'Lon: {lon}')
    print(f'Lat: {lat}')
    print(f'City: {city}')
    print(f'Country: {country}')
    #print(f"Lon: {position["longitude"]}")
    #print(f"Lat: {position["latitude"]}")

if __name__ == "__main__":
    main()


