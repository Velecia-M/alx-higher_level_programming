#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n_of_el = len(sys.argv) - 1

    if n_of_el == 0:
        print("0 arguments.")
    elif n_of_el == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(n_of_el))
    for x in range(n_of_el):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
