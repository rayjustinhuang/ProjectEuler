def isprime(number):
    test = 0
    if number == 0 or number == 1:
        return False
    for i in range(2, int(number ** (.5) + 1)):
        if number % i == 0:
            return False

    return True


def nthprime(index):
    count = 0
    finalcount = index
    prime = [1]
    # print(len(prime))
    while len(prime) < finalcount + 1:
        count += 1
        if not isprime(count):
            continue
        else:
            prime.append(count)
            index += 1
            # print(prime)

    return prime[finalcount]

# print(isprime(0))
n = input("Find the nth prime number; n = ")
print(nthprime(int(n)))
