from objects import *

def create_output(caches, filename=None):
    if filename is none:
        print(len(caches))
        for c in caches:
            print(str(c))

    else:
        with open(filename) as f:
            f.write(len(caches))
            for c in caches:
                f.write(str(c)+"\n")
        print("done writing into "+filename)
