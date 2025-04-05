import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from geopy.geocoders import Nominatim
import requests
import whois

print ("[( AUTHOR )]: UnKnown.")
print ("[( USAGE )]: use the country code eg.+639765469999.")
num = input("Enter the number you want to get infos: ")

# Enter the phone number you want to perform OSINT on
phone_number = phonenumbers.parse(num, "VN")

# Geolocation
geolocation = geocoder.description_for_number(phone_number, "en")

# Carrier
carrier_name = carrier.name_for_number(phone_number, "en")

# Print the results
print("Phone Number:", phone_number)
print("Geolocation:", geolocation)
print("Carrier:", carrier_name)
