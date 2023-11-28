#!/usr/bin/python3

for i in range(10):
    for j in range(10):
        number = i * 10 + j
        print("{:02d}".format(number), end='')
        if number != 99:
            print(", ", end='')
