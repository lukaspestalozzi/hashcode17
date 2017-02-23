from sys import stdin

'''
    Use 'cat input.in | python thisscript.py' to execute
'''

# This function solves the problem
def solveproblem(r, c, l, h, data):
    # Code extremely efficient solution here
    print(data)

# read the file v2
infile = stdin
line = infile.readline()
# Save problem parameters
v, e, r, c, x = list(map(int, line.split(" ")))

# advance to video sizes
line = infile.readline()
videosizes = line.rstrip('\n').split(" ")
print(videosizes)

# advance to endpoints
line = infile.readline()

for i in range(0, e):
    l, k = list(map(int, line.split(" ")))
    line = infile.readline()
    for i in range(0, k):
        c, lc = list(map(int, line.split(" ")))
        line = infile.readline()

# advance to request descriptions
line = infile.readline()
for i in range(0, r):
    rv, re, rn = list(map(int, line.split(" ")))



solveproblem(r, c, l, h, videosizes)
