inputfilename = "Problem 13 Input.txt"
inputFile = open(inputfilename)
inputContent = inputFile.read()
inputFile.close()

numbers = inputContent.split("\n")
length = len(numbers)
numbers = [float(i) for i in numbers]

sum = 0
for i in range(length):
    sum += numbers[i]

print(sum)