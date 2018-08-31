import os
currentDP = os.getcwd()
listOfFileNames = os.listdir(currentDP)
for name in listOfFileNames:
    if ".py" in name:
        print(name)