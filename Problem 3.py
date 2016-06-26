#Define prime factorization function

def primefactorize(number):
    factors = []
    for i in range(1,int(number**(.5)+1)):
        if number%i != 0 or i == 1:
            continue
        else:
            number = number/i
            factors.append(i)

    return factors

#n = input("Enter the integer to find the prime factors of: ")
#n = int(n)
#print("The prime factors of", n, "excluding 1 and itself are", primefactorize(n))

def isprime(number):
    test = 0
    for i in range(2,int(number**(.5)+1)):
        if number%i == 0 or number == 0:
            return False

    return True

#print(isprime(13195))

def largestprime(number):
    bigprime = 0
    if isprime(number):
        return number
    for i in range(int(number**(.5)+1),1,-1):
        if number%i != 0 or i == 1 or i == number:
            continue
        else:
            if isprime(i):
                bigprime = i
                break
            else:
                continue
    return bigprime

#n = input("Enter the integer to find the largest prime factor of: ")
#n = int(n)
#print("The largest prime factor of", n, "is", largestprime(n))

#print(largestprime(13195))
#print(primefactorize(largestprime(13195)))

print(largestprime(600851475143))
