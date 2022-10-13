# First import requests since website call will be made
import requests
# To tidy up the output
from pprint import pprint

# APIkey from Openweathermap
APIKey = "*Put your own API key here*"
# This is for the user to input
city = input("Enter a location: ")
# URL needs to be made of coordinates
# Coordinates need to come from geolocation API
# geolimit is 3, for three results max
geolimit = "3"
geourl = "https://api.openweathermap.org/geo/1.0/direct?q=" + city + "&limit=" + geolimit + "&appid=" + APIKey

# This request returns a list of dictionaries, maximum defined by geolimit
geodata = requests.get(geourl).json()
r1 = geodata[0]
r2 = ""
r3 = ""
# To avoid indexerror, second and third results are conditional on list length
if len(geodata) > 1:
    r2 = geodata[1]
if len(geodata) > 2:
    r3 = geodata[2]

# variable to store country code (ISO 3166 if it is important)
country1 = str(r1['country'])

# Redefining result variable as the two values for lat and lon keys, most important data
r1 = [str(r1['lat']), str(r1['lon'])]

if not r2 == "":
    country2 = str(r2['country'])
    r2 = [str(r2['lat']), str(r2['lon'])]
    lat2 = r2[0]
    lon2 = r2[1]

if not r3 == "":
    country3 = str(r3['country'])
    r3 = [str(r3['lat']), str(r3['lon'])]
    lat3 = r3[0]
    lon3 = r3[1]

# print(geodata)
# print(type(geodata))
# pprint(r1[0])
# pprint(r1[1])
# pprint(r2)
# pprint(r3)


if geodata == []:
    print("No results found for " + city + ".")

lat = r1[0]
lon = r1[1]
# exclude
ex = ""
# this should work
baseurl = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon + "&units=metric&appid=" + APIKey
if not r2 == "":
    baseurl2 = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat2 + "&lon=" + lon2 + "&units=metric&appid=" + APIKey
    wdata2 = requests.get(baseurl2).json()
if not r3 == "":
    baseurl3 = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat3 + "&lon=" + lon3 + "&units=metric&appid=" + APIKey
    wdata3 = requests.get(baseurl3).json()

# Request data from api
wdata = requests.get(baseurl).json()
# accessing temp which is a key within main which is within wdata:
temp = str(wdata['main']['temp'])
# The weather dictionary is actually inside of a list for seemingly no fukin reason??
wstatus = str(wdata['weather'][0]['main'])
# Uncomment this for the full monty
pprint(wdata)
print("")
print("")
print("")
print("")
print("")
print("In " + city + ", " + country1 + " the current temperature is " + temp + "°C.")
print("The weather condition is currently: " + wstatus + ".")
print("")
print("")
# Note to self: Next time write a function that instead of writing out the same code
if not r2 == "":
    print("Did you mean another " + city + " from another country? ")
    answer = input().lower()
    if answer in ["yes", "y", "ye"]:
        temp = str(wdata2['main']['temp'])
        wstatus = str(wdata2['weather'][0]['main'])
        print("In " + city + ", " + country2 + " the current temperature is " + temp + "°C.")
        print("The weather condition is currently: " + wstatus + ".")

    elif answer in ["no", "n"]:
        print("Exiting script...")
        exit()
    else:
        print("Please answer Yes or No.")


