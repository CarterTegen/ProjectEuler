import numpy as np

numbers = np.loadtxt('euler13.txt')
sum = 0
for number in numbers:
    sum += number

print(sum)