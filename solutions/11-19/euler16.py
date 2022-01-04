num = 2**1000
sum = 0
while num >= 1:
    sum += num%10
    print(sum, num)
    num = num//10

print(sum)
