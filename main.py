# NIKHIL GARG C0801980
# week 2 class code
# calling modules from other files.
import datetime


def areaOfCircle(radius):
    area = 3.14 * radius * radius
    return area


def displayDateTime():
    dt = datetime.datetime.now()
    return dt


def reverse_name():
    fname = input("Enter the first name:")
    lname = input("Enter the last name: ")
    print("The reverse of " + fname, lname + " is " + lname, fname)



