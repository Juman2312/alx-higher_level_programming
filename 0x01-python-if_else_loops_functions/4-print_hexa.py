#!/usr/bin/python3

output = ""
for i in range(100):
    if i < 10:
        output += "0{}".format(i)
    else:
        output += "{}".format(i)
    if i != 99:
        output += ", "

print(output)
