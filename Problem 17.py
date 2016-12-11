SpelledNumbers = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    1000: "onethousand",
}

count = 0

for i in range(1001):
    if i in SpelledNumbers:
        print(SpelledNumbers[i])
        count+=len(SpelledNumbers[i])
    elif int(i/10)>1:
        if i<100:
            print(SpelledNumbers[int(i/10)*10] + SpelledNumbers[i%10])
            count += len(SpelledNumbers[int(i/10)*10] + SpelledNumbers[i%10])
        elif i%100==0:
            print(SpelledNumbers[int(i/100)] + "hundred")
            count += len(SpelledNumbers[int(i/100)] + "hundred")
        elif i%100<20:
            print(SpelledNumbers[int(i / 100)] + "hundredand" + SpelledNumbers[i % 100])
            count += len(SpelledNumbers[int(i / 100)] + "hundredand" + SpelledNumbers[i % 100])
        elif i>120 and i%10==0:
            print(SpelledNumbers[int(i/100)] + "hundredand" + SpelledNumbers[int(i%100/10)*10])
            count += len(SpelledNumbers[int(i/100)] + "hundredand" + SpelledNumbers[int(i%100/10)*10])
        else:
            print(SpelledNumbers[int(i / 100)] + "hundredand" + SpelledNumbers[int(i % 100 / 10) * 10] + SpelledNumbers[i % 10])
            count += len(SpelledNumbers[int(i / 100)] + "hundredand" + SpelledNumbers[int(i % 100 / 10) * 10] + SpelledNumbers[i % 10])

print(count)