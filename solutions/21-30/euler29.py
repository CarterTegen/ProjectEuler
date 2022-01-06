
distinct_powers = set()

for a in range(2, 101):
    for b in range(2, 101):
        val = a**b
        distinct_powers.add(val)

print(len(distinct_powers))