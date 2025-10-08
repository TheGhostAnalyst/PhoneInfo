import phonenumbers
from phonenumbers import timezone, geocoder, carrier, NumberParseException, PhoneNumberType
import re
import time

def scan_num(number):
    num_reg = re.compile(r"^\+\d{1,2}\s?[-.]?\d{2,3}\s?[-.]?\d{2,3}\s?[-.]?\d{2,4}") 
    try:
        if num_reg.match(number):
            phone_no = phonenumbers.parse(number)
            country_code = phone_no.country_code
            national_num = phone_no.national_number
            time_zone = timezone.time_zones_for_number(phone_no)
            location = geocoder.description_for_number(phone_no, "en")
            service_prov = carrier.name_for_number(phone_no, "en")
            is_valid = phonenumbers.is_valid_number(phone_no)
            is_poss = phonenumbers.is_possible_number(phone_no)
            num_type = phonenumbers.number_type(phone_no)

            # readable number type map
            type_map = {
                PhoneNumberType.FIXED_LINE: "Fixed Line",
                PhoneNumberType.MOBILE: "Mobile",
                PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed Line or Mobile",
                PhoneNumberType.TOLL_FREE: "Toll Free",
                PhoneNumberType.PREMIUM_RATE: "Premium Rate",
                PhoneNumberType.SHARED_COST: "Shared Cost",
                PhoneNumberType.VOIP: "VoIP",
                PhoneNumberType.PERSONAL_NUMBER: "Personal Number",
                PhoneNumberType.PAGER: "Pager",
                PhoneNumberType.UAN: "Universal Access Number",
                PhoneNumberType.VOICEMAIL: "Voicemail",
                PhoneNumberType.UNKNOWN: "Unknown"
            }

            readable_type = type_map.get(num_type, "Unknown")

            print(f"Country Code: {country_code}")
            print(f"National Number: {national_num}")
            print(f"Timezone: {time_zone}")
            print(f"Location: {location}")
            print(f"Service provider: {service_prov}")
            print(f"Is Valid Number: {is_valid}")
            print(f"Is Possible Number: {is_poss}")
            print(f"Number Type: {readable_type}")

            seperator = '=' * 80
            with open('Number_Scan.txt', 'a') as f:
                f.write(f"\n{seperator}\n")
                f.write(f"Country Code: {country_code}\n")
                f.write(f"National Number: {national_num}\n")
                f.write(f"Timezone: {time_zone}\n")
                f.write(f"Location: {location}\n")
                f.write(f"Service provider: {service_prov}\n")
                f.write(f"Is Valid Number: {is_valid}\n")
                f.write(f"Is Possible Number: {is_poss}\n")
                f.write(f"Number Type: {readable_type}\n")

            print("\n✅ Scan saved to Number_Scan.txt")
            time.sleep(1)

        else:
            print(f"❌ Invalid number format: {number}")
    except NumberParseException as e:
        print(f"⚠️ Error parsing number: {e}")
        return

# Entry
ask = input('Enter number to scan with country code (e.g., +234XXXXXXXXXX): ')
print("🔎 Searching database...")
time.sleep(1)
scan_num(ask)
