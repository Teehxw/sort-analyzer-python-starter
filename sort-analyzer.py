# SORT ANALYZER STARTER CODE

import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS

def bubbleSort(anArray):
  for numCompare in range(len(anArray)-1,0, -1):
    for x in range(numCompare):
      if anArray[x] > anArray[x + 1]:
        anArray[x], anArray[x + 1] = anArray[x + 1], anArray[x]
  print(anArray)

def selectionSort(anArray):
  for fillSlot in range(len(anArray)):
    minIndex = fillSlot
    for x in range(fillSlot, len(anArray)):
      if anArray[x] < anArray[minIndex]:
        minIndex = x
    anArray[fillSlot], anArray[minIndex] = anArray[minIndex], anArray[fillSlot]

  print(anArray)

def insertionSort(anArray):
  for i in range(1, len(anArray)):
    insertVal = anArray[i]
    insertPos = i
    while insertPos > 0 and anArray[insertPos - 1] > insertVal:
      anArray[insertPos] = anArray[insertPos - 1]
      insertPos = insertPos - 1
      anArray[insertPos] = insertVal
  print(anArray)


"""
print(randomData[0:50])
print(reversedData[0:50])
print(nearlySortedData[0:50])
print(fewUniqueData[0:50])
"""

# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
startTime = time.time()
insertionSort(randomData)

endTime = time.time()
print(f"Insertion Sort Random Data: {endTime - startTime} seconds")
