import math

def initializeNumbers(quantity):
  array = []

  for x in range(quantity):
    array.append([])
#https://scikit-learn.org/sta#https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.htmlble/modules/generated/sklearn.tree.DecisionTreeClassifier.html
  return array

testNumbers = initializeNumbers(10)

def getArrayPosition(line):
  lastCharacterPosition = len(line) - 2
  digit = int(line[lastCharacterPosition])

  return digit

def getValuesFromString(line):
  formattedLine = []

  formattedLine = line.split(",")
  formattedLine.pop()

  return formattedLine


def addFormattedValuesToNumbers(formattedValues, arrayPosition, numbers):
  if arrayPosition > len(numbers) - 1: return False

  oldArray = numbers[arrayPosition]

  oldArray.append(formattedValues)

  numbers[arrayPosition] = oldArray

  return True

def getInputFileName(preffixFileName, fileExtension):
  inputFileName = "{}Train{}".format(preffixFileName, fileExtension)
  
  return inputFileName;

def calculateLastIndexToMaintain(percentage, length):
  value = math.floor((percentage / 100) * length)

  return value

def partionateData(digitData, percentageToMaintain):#https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
  length = len(digitData)

  lastIndex = calculateLastIndexToMaintain(
    percentageToMaintain, 
    length
  )

  return digitData[:lastIndex]


def writeLine(file, splittedData, index):

  print('to write', len(splittedData))
  
  for line in splittedData:
    formattedString = ','.join(line)
    formattedString += ',{}\n'.format(index)
    
    file.write(formattedString)

def writeResults(
  preffixFileName, 
  fileExtension, 
  numbers, 
  percentageToMaintain
):
  outputFileName = "{}Train__{}{}".format(preffixFileName, percentageToMaintain, fileExtension)

  file = open(outputFileName, "w");

  print('numbers', len(numbers[0]), percentageToMaintain)

  i=0
  total = 0
  for digitData in numbers:#https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
    
    splittedData = partionateData(digitData, percentageToMaintain)
   
    writeLine(file, splittedData, i)
    total += len(splittedData)
    
    i+=1

  file.close()


def main():
  preffixesFileNames = ['dig']
  percentages = [100, 50, 25]

  inputFileName = getInputFileName(preffixesFileNames[0], '.txt')
  
  file = open(inputFileName, "r")
  
  allLines = file.readlines()
  
  for line in allLines:
    formattedValues = getValuesFromString(line)
  
    arrayPosition = getArrayPosition(line)
    
    addFormattedValuesToNumbers(
      formattedValues, 
      arrayPosition,
      testNumbers
    )

  for preffix in preffixesFileNames:
    for percentage in percentages:  
      writeResults(
        preffix, 
        '.txt', 
        testNumbers, 
        percentage
      )
  
if __name__ == "__main__":
    main()