number_dict = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
    9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
    16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
    40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred",
    1000: "thousand"
}

def number_to_word(n):
    if 0 <= n <= 20:
        return number_dict[n]
    elif 20 < n <= 90 and n % 10 ==0:
        return number_dict[n]
    elif 20 < n <= 99:
        return f'{number_dict[n-n%10]} {number_dict[n%10]}'
    elif n % 100 == 0 and n != 1000:
        return f'{number_dict[n//100]} hundred'
    elif 0 < n <= 999:
        return f'{number_to_word(n-n%100)} and {number_to_word(n%100)}'
    else:
        return "one thousand"
    
sum = 0
for i in range(1, 1001):
    for letter in number_to_word(i):
        if 97 <= ord(letter) <= 122:
            sum += 1

print(sum)