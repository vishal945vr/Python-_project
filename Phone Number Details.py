# Phone Number Details 
import phonenumbers
from phonenumbers import  timezone,geocoder,carrier
# input for user
number=input("Enter Your Phone Number +__:")
# parse use for number details
phone=phonenumbers.parse(number)
# show the time zone 
time=timezone.time_zones_for_number(phone)
# uses for company name
carriers=carrier.name_for_number(phone,"en")
#register no
reg=geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(carriers)
print(reg)
