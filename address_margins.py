#!/usr/bin/env python3

# Created by : Izza Khalid
# Created on : November 2019
# This program accepts an address and then prints it


def full_address(name, street, city, province, postal_code, building=None):
    # return the full formal address

    if building != None:
        full_address = " " + building[0]
    full_address = name + " " + street, city, province, postal_code

    return full_address


def main():
    # gets a users name, Apt. number, street address, city province, PC
    building = None

    name = input("Enter your full name: ")
    question = input("Do you have an appartment number? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        building = input("Enter your appartment number: ")
    street = input("Enter your street address: ")
    city = input("Enter your city: ")
    province = input("Enter your province: ")
    postal_code = input("Enter your postal code: ")

    if building != None:
        address = full_address(name, building, street, city, province,
                               postal_code)
    else:
        address = full_address(name, street, city, province, postal_code)

    print(address)


if __name__ == "__main__":
    main()
