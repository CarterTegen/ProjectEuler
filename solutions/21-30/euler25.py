
fibonaccis = [0, 1, 1]

def fibonacci(i):
    if i < len(fibonaccis):
        return fibonaccis[i]
    else:
        val = fibonacci(i-1) + fibonacci(i-2)
        fibonaccis.append(val)
        return val

i = 1
while len(str(fibonacci(i))) < 1000:
    i+= 1

print(i)