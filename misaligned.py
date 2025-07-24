major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]

def getIndex(i,j):
    return i * 5 + j + 1

def getMajorMinor(i,j):
    return major_colors[i], minor_colors[j]

def print_color_map():
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            maj, mino = getMajorMinor(i,j)
            print(f'{getIndex(i,j)} | {maj} | {mino}')
    return len(major_colors) * len(minor_colors)


result = print_color_map()
assert(result == 25)
assert(getIndex(0,0) == 1)
assert(getIndex(0,1) == 2)
assert(getIndex(4,4) == 25)
assert(getIndex(2,2) == 13)
assert(getMajorMinor(0,0) == ('White','Blue'))
assert(getMajorMinor(0,3) == ('White','Brown'))
assert(getMajorMinor(3,4) == ('Yellow','Slate'))
print("All is well")
