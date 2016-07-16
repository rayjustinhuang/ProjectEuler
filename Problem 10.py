def isprime(number):
    test = 0
    for i in range(2,int(number**(.5)+1)):
        if number%i == 0 or number == 0:
            return False

    return True

sum = 2

for i in range(3,2000001,2):
    if isprime(i):
        sum += i
    else:
        continue

print(sum)