from time import time
import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input('Enter Your Number with +__ :  ')
phonenum = phonenumbers.parse(number)
tme = timezone.time_zones_for_number(phonenum)
car = carrier.name_for_number(phonenum,'en')
reg = geocoder.description_for_number(phonenum,'en')




print(phonenum)
print(tme)
print(car)
print(reg)