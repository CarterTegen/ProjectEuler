import numpy as np

def find_sum(n):
    sum = 0
    for i in range(1, int(n/2 + 1)):
        if n%i == 0:
            sum += i
    return sum

sum_amicable = 0
for i in range(1, 10001):
    sumi = find_sum(i)
    if sumi > i and find_sum(sumi)==i:
        sum_amicable += i + sumi


print(sum_amicable)