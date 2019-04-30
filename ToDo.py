# '------------------------------------------------------------------------#
#Title: To Do List, Assignment05
#Dev: Neil McCracken
#Date: April 29, 2019
#Change Log: (Who, When, What)
#   NMcCracken, 4/29/2019, Created Script
# '------------------------------------------------------------------------#
objFile = open("ToDo.txt", "r")  # 'Reading Text File into Program
myList = []  # 'Declaring my List
def show():  # 'Declaring a function so I can call it multiple times
    print("Current To Do List\n-----------------")
    for display in myList:  # 'For loop to iterate through MyList and manipulate data for output. https://canvas.instructure.com/courses/1133362/pages/book-5-dot-4-python-combining-lists-and-dictionaries (external link)
        first = display['task']
        second = display['priority']
        print(first, "--", second)
    #return first, second (My attempt to return values back to in Save Data Step(4)
    print("-----------------")

for line in objFile: # 'Reading the text file, line by line with a for loop into multiple dictionaries
    strChoice=line.split(",")  # 'Splitting at the comma and indexing
    a = strChoice[0]
    b = strChoice[1].strip('\n')
    dic = {"task": a, "priority": b}  # 'Placing indexed variables into the dictionary
    myList.append(dic)  # 'Appending dictionary to MyList

objFile.close()


show()  # 'Calling the function so I can display the ToDo list to user at opening

while strChoice != "5":  # 'While loop set to loop until user enters 5 to exit
    print(
    """
    Menu of Options

    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """

    )

    strChoice = input("Make a Selection: ")
    if strChoice == "1":
        show()  # 'Calling function to display ToDo List contents

    if strChoice == "2":  # 'Exactly like 5-2 lab to append new entries to MyList
        strTask = input("Enter a To Do task: ").lower()
        strPriority = input("Enter task level priority(low, high) ").lower()
        dicNewRow = {"task": strTask, "priority": strPriority}
        myList.append(dicNewRow)

    if strChoice == "3":
        delItem=input("Which task do you want to remove: ").lower()
        for i in range(len(myList)):  # 'Using a loop to delete items from the list, delItem matches task, item is removed from MyList
            if myList[i]['task'] == delItem:
                del myList[i]  # "https://www.geeksforgeeks.org/python-removing-dictionary-from-list-of-dictionaries/

    if strChoice == "4":
        #aReturn, bReturn=(show) Could only get 1 row of data when calling the function to avoid almost duplicate code
        f = open("ToDo.txt", "w")  # "Used the w to write over the existing document and update the list
        for display in myList:  # 'I tried to use another call to the show() function here but I could not get only on row on the return value
            first = display['task']
            second = display['priority']
            f.write(first + "," + second + "\n")
        continue
        f.close()

    if strChoice == "5":
        print("Data Saved To File")
        exit()  # 'Data saved when user exits program






























