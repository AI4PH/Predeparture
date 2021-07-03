import pandas as pd

def getData():
    while(True):
        nameInput = input("Enter a list of names separated by commas: \n")
        allNames = nameInput.split(',')
        majorInput = input("Enter a list of majors separated by commas: \n")
        allMajors = majorInput.split(',')
        if len(allMajors) != len(allNames):
            print("The number of names and majors are not equal!\n")
        else:
            break
    print(allNames)
    return [allNames, allMajors]

def printMajors(names, majors):
    majorDict = {}
    for i in range(len(names)):
        majorDict[names[i]] = majors[i]
    print(majorDict)
    return majorDict

def printFrequency(majorsDict):
    print("")
    majorsData = pd.DataFrame.from_dict(majorsDict, orient='index')
    print(majorsData)
    print('Number of each major:')
    print(majorsData.value_counts())


[names, majors] = getData()
majorsDict = printMajors(names, majors)
printFrequency(majorsDict)







