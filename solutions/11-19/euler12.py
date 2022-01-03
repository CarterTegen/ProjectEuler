
def num_factors(n):
    if n==1:
        return 1
    elif n==3:
        return 2

    count = 0
    for i in range(1, int(n**.5)+1):

        if n%i == 0:
            count += 1
            

    return count*2

num_divisors = 0
count = 1
i = 1
while num_divisors < 500:
    num_divisors = num_factors(i)
    print(i, num_divisors)
    count += 1
    i += count

