def countWordsFromAFile():
    fileName = input("Enter the file name = ")
    fileObj = open(fileName, "r")
    fileLines = fileObj.readlines()
    numberOfWords = 0

    for line in fileLines:
        words = line.split()
        print(words)
        numberOfWords = numberOfWords+len(words)
        
    print("Total number Of Words =")
    print(numberOfWords)
# countWordsFromAFile()

def writeFile():
    fileNmae = input("Enter the file name = ")
    fileObj = open(fileNmae, "r+w")
    content = fileObj.read()
    content.append("We want the legendary CORONA to go away as soon as possible")
    fileObj.write(content)
    fileObj.close()

writeFile()