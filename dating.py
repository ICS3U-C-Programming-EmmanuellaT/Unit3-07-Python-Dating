#!/usr/bin/env python3
# Created By: Emmanuella Taiwo
# created on 26th Oct, 2026
# This program asks the for an age number as a string
# and casts it into an integer and
# displays if the grand parents approve or not


def main():
    # this function checks if the age is between 25 and 40
    # and displays if the grand parents approve or not
    # input
    age_as_string = input("Enter your age: ")
    print("{age}".format(age=age_as_string))
    # process & output
    try:
        age_as_integer = int(age_as_string)
        if age_as_integer >= 25 and age_as_integer <= 40:
            print("The grand parents approve".format(age_as_string))
        else:
            print("The grand parents do not approve".format(age_as_string))
    except Exception:
        print("Invalid input, please enter a number")


if __name__ == "__main__":
    main()
