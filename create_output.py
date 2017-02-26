from objects import *

def create_output(caches, filename=None):
    s = str(len(caches))
    for c in caches:
        s += "\n" + str(c.output_format())
    print(s)
    if filename is not None:
        with open(filename, 'w') as f:
            f.write(s)
