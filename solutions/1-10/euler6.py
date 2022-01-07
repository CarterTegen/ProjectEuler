n = 100
sumSquare = 0
squareSum = 0
for i in range(1, n + 1):
    squareSum = squareSum + i
    sumSquare = sumSquare + i**2

squareSum = squareSum**2

print(squareSum - sumSquare)
