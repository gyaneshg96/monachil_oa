"""
Script for getting rainy days for a given city as input
"""
from rain_data import RainData, get_city_data


# rain data from .
# https://coastwatch.pfeg.noaa.gov/erddap/griddap/chirps20GlobalPentadP05.html
# used dataset:
# https://coastwatch.pfeg.noaa.gov/erddap/griddap/chirps20GlobalPentadP05.csv?precip%5B(2022-07-25T00:00:00Z):1:(2022-07-26T00:00:00Z)%5D%5B(30.0):1:(42.0)%5D%5B(-123.0):1:(-113.0)%5D    

city_name = str(input("Enter city name:[San Jose]") or "San Jose")
c_lat, c_long = get_city_data(city_name)

rain_data = RainData()
rain_data.get_rainy_days("chirps20GlobalPentadP05_2b5a_36a5_f134.csv")
rain_data.get_days_for_city(c_lat, c_long)
rain_data.print_days()


               

