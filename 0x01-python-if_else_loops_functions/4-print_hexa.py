#!/usr/bin/python3

output = ""
for i in range(10):
    for j in range(i, 10):
        if i != j:
            output += str(i) + str(j) + ", "

output = output[:-2]  # Remove the trailing comma and space
print(output)
