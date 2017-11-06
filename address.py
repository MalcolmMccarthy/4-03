# created by malcolm
#on oct 2017
#for ics3u
#displays Apt. Number Street Address City Province and postal code


def print_address(street_address, city, province, postal_code, apartment_number = ''):
    street_address = raw_input("enter street address")
    city = raw_input("enter your city")
    province = raw_input("enter your province")
    postal_code = raw_input("enter your postal code")
    apartment = raw_input("do you have an apartment #? (y/n)")
    if apartment == 'y':
        apartment_number = raw_input("enter apartment #")
        print_address(street_address, city, province, postal_code, apartment_number)
    else:
        print_address(street_address, city, province, postal_code)
        
print_address("", "", "", "")
