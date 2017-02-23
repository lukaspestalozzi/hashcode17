import fileinput

# Use 'cat input.in | python thisscript.py' to execute
for line in fileinput.input():
    if fileinput.isfirstline():
        # Save problem parameters
        r, c, l, h = list(map(int, line.split(" ")))
    else:
        # Solve Problem
        print(r, c, l, h)
