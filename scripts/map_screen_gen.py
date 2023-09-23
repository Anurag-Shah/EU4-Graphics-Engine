from PIL import Image
import numpy as np

array = np.zeros([160, 200, 3], dtype=np.uint8)

r = 1
g = 0
b = 0

for j in range(160):
    for i in range(200):
        array[j][i][0] = r
        array[j][i][1] = g
        array[j][i][2] = b
        b += 1
        if b == 256:
            b = 0
            g += 1
        if g == 256:
            g = 0
            r += 1

# Convert array to image
im = Image.fromarray(array)
im.save("e.png")