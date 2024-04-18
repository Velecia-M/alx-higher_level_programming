#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    len_of_args = len(argv)
    if len_of_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        exit(1)
    a = int(argv[1])
    operator = int(argv[2])
    b = int(argv[3])
    if operator == '+':
        print(f"{a} {operator} {b} = (add(a, b))\n")
    elif operator == '-':
        print(f"{a} {operator} {b} = (sub(a, b))\n")
    elif operator == '*':
        print(f"{a} {operator} {b} = (mul(a, b))\n")
    elif operator == '/':
        print(f"{a} {operator} {b} = (div(a, b))\n")
    else:
        print("Unknown operator. Available operators: +, -, * and /\n")
        exit(1)
