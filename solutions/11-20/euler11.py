import numpy as np
array = np.loadtxt('euler11.txt', delimiter=' ')
max = -1

for i in range(len(array)):
    for j in range(len(array[0])):

        # Horizontal
        if j <= len(array) - 4:
            product = array[i][j] * array[i][j + 1] * \
                array[i][j + 2] * array[i][j + 3]
            if product > max:

                max = product

        # Vertical
        if i <= len(array) - 4:
            product = array[i][j] * array[i + 1][j] * \
                array[i + 2][j] * array[i + 3][j]
            if product > max:

                max = product

        # Diagonal down right
        if i <= len(array) - 4 and j <= len(array) - 4:
            product = array[i][j] * array[i + 1][j + 1] * \
                array[i + 2][j + 2] * array[i + 3][j + 3]
            if product > max:

                max = product

        # Diagonal down up
        if i >= 3 and j <= len(array) - 4:
            product = array[i][j] * array[i - 1][j + 1] * \
                array[i - 2][j + 2] * array[i - 3][j + 3]
            if product > max:
                max = product
print(max)
