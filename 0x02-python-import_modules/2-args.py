#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv
    n_of_el = len(arg) - 1
    if n_of_el > 1:
        print("{} arguments:".format(n_of_el))
        for x in range(1, n_of_el +1):
            print("{}: {}".format(x, arg[x]))
    elif n_of_el == 0:
        print("{} arguments.".format(n_of_el))
    else:
        print("{} arguments:".format(n_of_el))
        print("{}: {}".format(n_of_el, arg[1]))
