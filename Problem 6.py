def sumsquarediff(naturalnumber):
    sumofsquares = 0
    count = 0
    for i in range(naturalnumber+1):
        count += i
        sumofsquares += i**2

    squareofsum = count**2
    #print(squareofsum)
    #print(count)
    #print(sumofsquares)
    difference = squareofsum - sumofsquares

    return difference

n = input("Enter the natural number you want to find the sum square difference of: ")
print(sumsquarediff(int(n)))
