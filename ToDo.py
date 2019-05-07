#-------------------------------------------------#
# Title: Assignment06:  Organizing data with functions and classes
# Dev:  Neil McCracken
# Date:  May 4th, 2019
# ChangeLog: (Who, When, What)
#   NMcCracken 05/04/2019, Created Script

#-------------------------------------------------#
#-----------------------Data----------------------#
lstMyList=[]
myDic={None}
objFile = open("ToDo.txt", "r")  # 'Reading Text File into Program
strChoice=None

##Input/Output##
class MyClass(object):
    """Group of Functions"""
    @staticmethod
    def read_file():
        '''Turns each line of data from text.file into a dictionary'''
        for line in objFile:  # 'Reading the text file, line by line with a for loop into multiple dictionaries
            strTemp = line.split(",")  # 'Splitting at the comma and indexing
            dic = {'task': strTemp[0], "priority": str(strTemp[1].strip("\n").strip(" "))}  # 'Placing indexed variables into the dictionary
            lstMyList.append(dic)  # 'Appending dictionary to MyList
        return lstMyList

    @staticmethod
    def ShowList(lstMyList):
        '''Functin to display list throughout program'''
        print("Current To Do List\n-------------------")
        for row in lstMyList:
            print(row['task']+"--" + row['priority'])
        print("-------------------")
    @staticmethod
    def AddList(value1, value2):
        '''Function adds new to do list items into Dictionaries'''
        dicNewRow = {"task": value1, "priority": value2}
        lstMyList.append(dicNewRow)

    @staticmethod
    def DelList(itemDel, lstMyList):
        '''Function that deletes dictionaries from list'''
        blnItemRemoved = False
        intCounter=0
        while (intCounter < len(lstMyList)):
            if itemDel == str(list(dict(lstMyList[intCounter]).values())[0]).lower():
                del lstMyList[intCounter]
                blnItemRemoved = True
            intCounter += 1
        return blnItemRemoved

    @staticmethod
    def ItemStatus(value1):
        '''Function that evaluates boolean to let user know if item was removed'''
        if value1 == True:
            print("Item was removed")
        if value1 == False:
            print("Item was not removed, please try again.")

    @staticmethod
    def SaveToFile(value1):
        '''Function that saves data to file'''
        if value1=="y":
            f = open("ToDo.txt", "w")  # "Used the w to write over the existing document and update the list
            for display in lstMyList:  # 'I tried to use another call to the show() function here but I could not get only on row on the return value
                first = display['task']
                second = display['priority']
                f.write(first + "," + second + "\n")
            f.close()
        else:
            print("Please try again or exit the program")

    @staticmethod
    def ExitProgram():
        '''Function that allows user to exit program '''
        exit()


    @staticmethod
    def MakeSelection():
        '''function that allows user to make selection within while loop'''
        strChoice = input("make a selction, 1-5: ")
        return strChoice

    @staticmethod
    def DisplayMenu():
        '''function that displays the menu of options'''
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
##End of MyClass
#Step 1
MyClass.read_file()  # 'Load file into dictionaries and list
MyClass.ShowList(lstMyList)  #  'Display List to User, Step 3
while True:
    MyClass.DisplayMenu()  # 'Step 2, display menu of choices to user with function call
    strChoice=MyClass.MakeSelection()  # "Return variable from function call
    if strChoice== "1":
        MyClass.ShowList(lstMyList)  # 'Displays current list with function call
    elif strChoice== "2":
        value1=input("What is the task?: ")  # 'Step 4, User can add new item to list
        value2=input("What is the priority? ")
        MyClass.AddList(value1, value2)  # 'Positional arguments expected with function call
        MyClass.ShowList(lstMyList)  # 'Display the new items to user
    elif strChoice == "3":
        itemDel=input("What task would you like to remove?: ")
        blnItemRemoved=MyClass.DelList(itemDel, lstMyList)  # 'Step 5, Remove a new item from the list
        MyClass.ItemStatus(blnItemRemoved)
        MyClass.ShowList(lstMyList)
    elif strChoice == "4":  # 'Step 6, Save current list to file, overwriting previous list
        saveFile=input("Would you like to save the new list to file?: y/n")
        MyClass.SaveToFile(saveFile)
    elif strChoice == "5":  # 'Step 7, User can exit program
        MyClass.ExitProgram()
    else:
        print("try again")







