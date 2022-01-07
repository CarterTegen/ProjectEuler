def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = 20
lattice_paths = int(factorial(2 * n) / (factorial(n)**2))
print(lattice_paths)
