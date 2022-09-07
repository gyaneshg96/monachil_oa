"""Contains helper classes and functions for getting rainy days 

"""

import csv
from numpy import void
import requests


DISTANCE_THRESHOLD = 0.05
RAIN_THRESHOLD = 8.0


def get_city_data(city_name: str)-> tuple:
    """ Returns the latitude and longitude for a given city name
    Args: 
        city_name : The name of city for the coordinates to be found

    Returns:
        A tuple having the latitude and longitude
    
    Raises:
        Exceptions when the request cannot be fetched and there does not exist any city with the name
    """
    response = requests.get(f"https://nominatim.openstreetmap.org/search.php?city={city_name}&format=jsonv2&namedetails=0&addressdetails=0&limit=1")

    if response.status_code == 200:
        city_data = response.json()
    else:
        raise Exception("Request cannot be found")

    try:
        c_lat=city_data[0]['lat']
        c_long=city_data[0]['lon']
        return c_lat, c_long

    except Exception as e:
        raise Exception("No such city")
    

class RainData:
    """ Helper class for fetching, processing and printing the rain data
    """
    def __init__(self):
        self.dates = []
        self.rain_data = []

    def get_rainy_days(self, filename: str) ->void:
        """ Takes in a file name, and reads it
        Args :
            filename : Name of the csv file containing the rain status based on time and coordinates
        """
        with open(filename,"r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                line_count += 1
                print(line_count)
                if line_count <= 2:
                    continue
                elif line_count >= 10e10:
                    break
                self.rain_data.append(row)
            csv_file.close()

    def get_days_for_city(self, c_lat: str, c_long: str) ->void:
        """Given the latitude and longitude, filters out those rows which are rainy
        
        Args :
            c_lat : latitude of the place in string
            c_long : longitude of the place in string

        """
        for row in self.rain_data:
            t,lat,lon,rain=row
            t=t[:10]
            lat_diff=abs(float(lat)-float(c_lat))
            lon_diff=abs(float(lon)-float(c_long))
            if rain != "NaN":
                if float(rain) >= RAIN_THRESHOLD:
                    if lat_diff < DISTANCE_THRESHOLD and  lon_diff< DISTANCE_THRESHOLD:
                        self.dates.append((t,rain))
    
    def print_days(self)->void:
        """Prints the data 
        """
        for item in self.dates:
            print(item)
        print(f"Number of rainy 5-days: {len(self.dates)}")