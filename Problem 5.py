##def smallestmultipleunder(number,multiple,step=1):
##    count = 0
##    while count < number:
##        for i in range(multiple+1,step):
##            if count%i == 0:
##                continue    
##            else:
##                break
##        count += 1
##
##    return count

#Brute force approach
def smallestmultiple(multiple):
    activenum = (multiple*(multiple-1))-(multiple-1)
    test = 0
    while test < multiple:
        activenum += multiple-1
        for i in range(1,multiple+1):
            if activenum%i == 0:
                test += 1
                #print("test:",test)
            else:
                test = 0
                break
            
        #print("count:",activenum)

    return activenum

#print(smallestmultiple(20))

#Project Euler approach

#Prime number checker
def isprime(number):
    test = 0
    if number == 0 or number == 1:
        return False
    for i in range(2,int(number**(.5)+1)):
        if number%i == 0:
            return False

    return True

#Smallest multiple algorithm
def eulersmallestmultiple(k):

#Prime number list generation
    index = k
    count = 0
    finalcount = index
    prime = [1]
    #print(len(prime))
    while len(prime) < finalcount+1:
        count += 1
        if not isprime(count):
            continue
        else:
            prime.append(count)
            index += 1

#Proposed approach
    import math
    N = 1
    i = 1
    check = True
    limit = math.sqrt(k)
    a = list(range(0,k+1))
    print(a[1])

    while prime[i] <= k:
        a[i] = 1
        if check:
            if prime[i] <= limit:
                a[i] = math.floor(math.log(k)/math.log(prime[i]))
            else:
                check = False
        N = N * prime[i]**a[i]
        i += 1

    return N

print(eulersmallestmultiple(20))
