inputfilename = "p022_names.txt"
inputFile = open(inputfilename)
inputContent = inputFile.read()
inputFile.close()

namesList = inputContent.split(",")
namesList.sort()

Alphabet = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,
            "L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,
            "V":22,"W":23,"X":24,"Y":25,"Z":26,"\"":0}

totalScore = 0
for name in range(0, len(namesList)):
    print(namesList[name])
    nameScore = 0
    for i in range(len(namesList[name])):
        nameScore += Alphabet[namesList[name][i]]

    totalScore += (name + 1) * nameScore  # sum([int(Alphabet[namesList[name][i]]) for i in namesList[name]])

print(totalScore)
