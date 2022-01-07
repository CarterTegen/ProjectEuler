with open('euler22.txt', 'r') as file:
    data = sorted(file.readline().replace('"', '').split(','))

print(data[937])
count = 1
total_sum = 0
for value in data:
    sum = 0
    for char in value:
        sum += ord(char) - 64

    total_sum += sum * count
    count += 1

print(total_sum)
