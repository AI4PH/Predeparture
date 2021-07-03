#!/usr/bin/env python
# coding: utf-8

# In[1]:


listOfNames = [] #empty list
listOfMajors = [] #empty list
listOfTravel = [] #empty list

def userinfoInput (number): 
    number = int(input("how many students' data do you wish to enter?\n")) #ask user for a number
    for i in range(number):
        username = input("What is your name?") #ask user for student name
        print("Your name is", username)
        listOfNames.append(username)
        major = input("What is your major?") #ask user for student major
        print("Your major is", major)
        listOfMajors.append(major)
        travel = input("How do you travel to campus?") #ask user for student mode of travel
        print("You travel to campus via", travel)
        listOfTravel.append(travel)
        print("\nthanks!")
    print(listOfNames, listOfMajors, listOfTravel) 
userinfoInput(3)

dictionary=dict(zip(listOfNames, listOfMajors)) #students and their majors #Source:https://stackoverflow.com/questions/49087080/python-dictionaries-with-lists-from-user-input-how-to-solve-this
print(dictionary)

dictionarytwo=dict(zip(listOfNames, listOfTravel)) #students and their modes of travel to campus
print(dictionarytwo)

Namedictionary=dict(zip("name", listOfNames)) #student names
Majorsdictionary=dict(zip("major", listOfMajors)) #student majors
Traveldictionary=dict(zip("travel", listOfTravel)) #student modes of travel to campus
print(Namedictionary, Majorsdictionary, Traveldictionary)

import numpy as np
arr = np.array([listOfTravel])
print(np.sort(arr))


# In[ ]:




