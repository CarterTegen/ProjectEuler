import numpy as np

for i in range(1000):
    for j in range(i, 1000):

        c = np.sqrt(i**2 + j**2)

        if c != int(c):
            continue

        if i + j + c == 1000:
            print(i*j*c)
