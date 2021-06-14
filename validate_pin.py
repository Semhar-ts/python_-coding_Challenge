
def validate_pin(pin):
    return len(pin)in (4, 6) and pin.isdigit()

print ('validating pin.')
print ('pin are 4 digit or 6 digit , and only number .')
print ( " ex.pin = '1234' or pin = '123456' >> True ")
print ( " ex.pin = '123' or pin = '12345a' >> False \n ")

pin = input('Enter pin:')
print (" the result :")
print (validate_pin(pin))
