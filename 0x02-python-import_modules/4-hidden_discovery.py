#!/usr/bin/python3
import marshal

def print_hidden_names():
    with open('hidden_4.pyc', 'rb') as file:
        code = marshal.load(file)

    names = set()
    for const in code.co_consts:
        if isinstance(const, str) and not const.startswith('__'):
            names.add(const)

    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    print_hidden_names()