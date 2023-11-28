#!/usr/bin/python3
def uppercase(string):
    uppercase_string = ""
    for char in string:
        if ord(char) >= 97 and ord(char) <= 122:
            uppercase_string += chr(ord(char) - 32)
        else:
            uppercase_string += char
    print("{}".format(uppercase_string))
