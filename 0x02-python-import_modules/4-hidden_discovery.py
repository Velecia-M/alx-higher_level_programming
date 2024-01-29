#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    
    names = dir()
    for x in range(0, len(names)):
        if names[x][:2] != "__":
            print("".format(names[x]))
