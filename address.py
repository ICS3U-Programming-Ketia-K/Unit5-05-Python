#!/usr/bin/env python3

# Created by: Ketia Gaelle Kaze
# Created on: Jan. 25, 2022
# This program asks the user for their address
# and print it back in a proper format.

def format_address(name, answer, street_num, street_name, city,
                   province, postal_code, apt_num=None):
    # format strings and sets them as uppercase
    can_post_address = name.upper() + "\n" + street_num + " " \
                       + street_name.upper() + "\n" + city.upper() \
                       + " " + province.upper() + " " + postal_code.upper()

    # ask  if user lives in an apartment and add it to the address
    if answer == "y":
        can_post_address = name.upper() + "\n" + apt_num \
                           + "-" + street_num + " " + street_name.upper() \
                           + "\n" + city.upper() + " " + province.upper() \
                           + " " + postal_code.upper()
        return can_post_address
    # copies the format to the main function
    return can_post_address


# get input from user and displays the address
def main():
    apt_num_user = None

    # display opening message
    print("This program formats an address to a Canadian mailing address.")
    print("")

    # gets input from the user
    full_name_user = input("Enter your full name: ")
    answer_user = input("Do you live in an apartment? (y/n): ")

    # check if user lives in an apartment
    if answer_user == "y":
        apt_num_user = input("Enter your apartment number: ")

    # get input from the user
    street_num_user = input("Enter your street number: ")
    street_name_user = input("Enter your street name and "
                             "type: ")
    city_user = input("Enter your city: ")
    province_user = input("Enter your province (as an abbreviation): ")
    postal_user = input("Enter your postal code: ")

    # assign variable to function that formats the address
    if apt_num_user is not None:
        user_address = format_address(full_name_user, answer_user,
                                      street_num_user, street_name_user,
                                      city_user, province_user,
                                      postal_user, apt_num_user)
    else:
        user_address = format_address(full_name_user, answer_user,
                                      street_num_user, street_name_user,
                                      city_user, province_user,
                                      postal_user)
    print("")
    print("Your Canadian mailing address is:\n")
    print(user_address)


if __name__ == "__main__":
    main()
