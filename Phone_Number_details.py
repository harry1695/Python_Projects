import phonenumbers
from phonenumbers import geocoder, carrier, timezone

number = "Country_code Your Phone No."

ch_number = phonenumbers.parse(number, "CH")
country_name = geocoder.description_for_number(ch_number, "en")
print(country_name)
service_number = phonenumbers.parse(number, "RO")
carrier_name = carrier.name_for_number(service_number, "en")
print(carrier_name)
gb_number = phonenumbers.parse(number, "GB")
time_zone = timezone.time_zones_for_number(gb_number)
print(time_zone)