def is_prime(num):
    if num > 1:

        # Iterate from 2 to n / 2
        for i in range(2, int(num / 2) + 1):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
                break
        else:
            return True

    else:
        return False


if __name__ == '__main__':

    numPrime = 2
    n = 1

    while numPrime <= 10001:
        if is_prime(n):
            print(numPrime, n)
            numPrime += 1

        n += 2
