import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import NumberParseException
import re
import time
import os

def scan_num(number):
    num_reg = re.compile(r"\+\d{1,2}\s?[-.]?\d{2,3}\s?[-.]?\d{2,3}\s?[-.]?\d{2,4}")
    try:
        if num_reg.match(number):
            phone_no = phonenumbers.parse(number)
            country_code = phone_no.country_code
            national_num = phone_no.national_number
            time_zone = timezone.time_zones_for_number(phone_no)
            location = geocoder.description_for_number(phone_no, "en")
            service_prov = carrier.name_for_number(phone_no, "en")
            is_valid = phonenumbers.is_valid_number(phone_no)
            is_poss =  phonenumbers.is_possible_number(phone_no)
            print(f"Country Code: {country_code}")
            print(f"National Number: {national_num}")
            print(f"Timezone: {time_zone}")
            print(f"Location: {location}")
            print(f"Service provider: {service_prov}")
            print(f"Is Valid Number: {is_valid}")
            print(f"Is Possible Number: {is_poss}")
        else:
            print(f'Invalid number format {number}')
    except NumberParseException as e:
        print(f"Error parsing number: {e}")
        return

ask = input('Enter number to scan with country code (eg., +123XXXXXXX...): ')
print("Searching Database......")
time.sleep(1)
scan_num(ask)
