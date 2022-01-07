def is_palindrome(n):
    orig = n
    flipped = 0
    while n >= 1:
        ones = n % 10
        flipped = flipped * 10 + ones
        n = int(n / 10)

    return orig == flipped


sum = 0
for i in range(1, 10**6):
    binary = bin(i)

    if(is_palindrome(i) & is_palindrome(int(binary[2:]))):
        print(i)
        sum += i

print(sum)
