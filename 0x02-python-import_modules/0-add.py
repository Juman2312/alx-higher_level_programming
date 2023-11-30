#!/usr/bin/python3
from operator import add
import os

a = 1
b = 2

add_file_path = os.path.join(os.path.dirname(__file__), 'add_0.py')
exec(open(add_file_path).read())

result = add(a, b)

print("{} + {} = {}".format(a, b, result))