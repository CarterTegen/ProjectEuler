factorial_lookup = {
    0: 1,
    1: 1,
    2: 2,
    3: 6,
    4: 24,
    5: 120,
    6: 720,
    7: 5040,
    8: 40320,
    9: 362880
}

sum = 0
for i in range(3, 10**6):

    orig_i = i

    i_sum = 0
    while i >= 1:
        
        dig = i%10
        #print(orig_i, dig)
        i_sum += factorial_lookup[dig]
        #print(orig_i, dig, i_sum)
        i = i//10

    #print(orig_i, i_sum)
    if orig_i == i_sum:
        print(orig_i)
        sum += i_sum

print(sum)