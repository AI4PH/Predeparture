#%%
import matplotlib.pyplot as plt # import this library to help plot student grades

namelist = [] # initialize list
majorlist = [] # initialize list

def StudentInformation (number): # function that takes in 1 argument - the number of students' data we are looking at
    for i in range(number): # for loop to run through number of students' inputted
        name = input("Please enter student name\n") 
        major = input("Please enter student major\n")
        namelist.append(name) # add to list
        majorlist.append(major) # add to list
 
    studentDictionary = dict(zip(namelist,majorlist)) # combine two lists into one dictionary
    print("Thank you for entering all your student data.") # print statement
    getName = input('Please provide a previously entered student name exactly as entered previously \n') # ask user for which student they'd like to explore further
    print(getName,"'s major is",studentDictionary[getName]) # print major of the selected student

    print("thank you for selecting", getName) # confirm selection of student name
    numCourses = int(input("How many classes is this student enrolled in this semester? \n")) # number of courses
    print(getName, "is enrolled in the following number of classes", numCourses) 

    gradelist = [] # initialize list 
    subjectlist = [] # initialize list

    for i in range(numCourses): # for loop to run through number of courses inputted by user
        subject = input("Please enter subject name\n")
        grade = float(input("Please insert student grade \n"))
        subjectlist.append(subject)   # add subject to list
        gradelist.append(grade) # add grade to list
    gradeDictionary = dict(zip(subjectlist,gradelist)) # create dictionary
        

    print("The student's grades for the semester are as follows:", gradeDictionary) # print the dictionary
    plt.bar(subjectlist, gradelist) # grade the student's grades in a bar plot

    return plt.bar(subjectlist, gradelist)


StudentInformation(2) # call function







# %%
