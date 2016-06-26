#Declare variables
ID = 0
a = 0
b = 1
fibsum = 0

#Fibonacci sequence
while len(str(a))<1000:
    temp = a
    a = b
    b = temp + b
    ID += 1
    #print(ID, ":", a)
    if a%2 == 0:
        fibsum += a

print(ID)
