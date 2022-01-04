def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

val = factorial(100)
sum = 0
while val >= 1:
    sum += val%10
    val = val//10

print(sum)