

def collatz(n, initial):
    #Base Case
    if n == 1:
        return 1
    if n < initial:
        return collatz_sequence[n]

    if n%2 == 0:
        return collatz(int(n/2), initial) + 1
    else:
        return collatz(int(3*n+1), initial) + 1


collatz_sequence = [0]


for n in range (1, 1000001):
    collatz_sequence.append(collatz(n, n))

max_sequence = max(collatz_sequence)
print(f"The number with the largest collatz sequence is {collatz_sequence.index(max_sequence)} with a length of {max_sequence}.")
