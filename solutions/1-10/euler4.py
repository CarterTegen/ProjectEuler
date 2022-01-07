def is_palindrome(n):
    orig = n
    flipped = 0
    while n >= 1:
        ones = n % 10
        flipped = flipped * 10 + ones
        n = int(n / 10)

    return orig == flipped


if __name__ == '__main__':
    palindromes = []
    for i in range(100, 999):
        for j in range(i, 999):
            if is_palindrome(i * j):
                palindromes.append(i * j)

    print(max(palindromes))
