import fileinput

'''
    Use 'cat input.in | python thisscript.py' to execute
'''

# This function solves the problem
def solveproblem(r, c, l, h, data):
    # Code extremely efficient solution here
    print(data)

# read the file
for line in fileinput.input():
    if fileinput.isfirstline():
        # Save problem parameters
        r, c, l, h = list(map(int, line.split(" ")))
        # create some data structures for problem data
        data = []
    else:
        # read input
        data.append(line.rstrip('\n'))

solveproblem(r, c, l, h, data)
