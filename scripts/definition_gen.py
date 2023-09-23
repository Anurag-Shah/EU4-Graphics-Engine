START_INDEX = 8
WIDTH = 200
HEIGHT = 160

r = 1
g = 0
b = 0
for i in range(START_INDEX, START_INDEX + WIDTH * HEIGHT):
    print(f"{i};{r};{g};{b};{i};x")
    b += 1
    if b == 256:
        b = 0
        g += 1
    if g == 256:
        g = 0
        r += 1