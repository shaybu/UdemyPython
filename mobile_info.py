import phonenumbers
from phonenumbers import geocoder, carrier, timezone

phone_number = "+972523552499"  # Enter phone number

# Parse the phone number
parsed_number = phonenumbers.parse(phone_number)

# Get country information
country = geocoder.description_for_number(parsed_number, "en")

# Get carrier information
phone_carrier = carrier.name_for_number(parsed_number, "en")

# Check if the phone number is valid and possible
is_valid = phonenumbers.is_valid_number(parsed_number)
is_possible = phonenumbers.is_possible_number(parsed_number)

# Get the line type
line_type = phonenumbers.number_type(parsed_number)

# Get the time zone
time_zones = timezone.time_zones_for_number(parsed_number)

print(f"Country: {country}")
print(f"Carrier: {phone_carrier}")
print(f"Valid: {is_valid}")
print(f"Possible: {is_possible}")
# Corrected line type output
# print(f"Line Type: {phonenumbers.PhoneNumberType(line_type).name}")
print(f"Time Zone(s): {', '.join(time_zones)}")
