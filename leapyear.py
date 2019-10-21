#!/usr/bin/env python3

# Created by: Paul M
# Created on: October 2019
# This program calculates leap Years


def main():
# This function figures out leap years


        # input
        print("This program determines leap years")
        print("")
        year = input("PLease enter a year: ")
        print("")

        # process
        try:
            year_int = int(year)
            if year_int < 0:
                print("Please enter a valid year")
                return
            if (year_int % 4) == 0:
                if (year_int % 100) == 0:
                    if (year_int % 400) == 0:
                        print("{} is a leap year".format(year_int))
                    else:
                        print("{} is not a leap year".format(year_int))
                else:
                    print("{} is a leap year".format(year_int))
            else:
                print("{} is not a leap year".format(year_int))
        except(ValueError):
            print("Please enter a valid year")


if __name__ == "__main__":
    main()
