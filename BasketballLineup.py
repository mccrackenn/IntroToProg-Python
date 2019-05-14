#-------------------------------------------------#
# Title: Assignment07:  Pickling and Exceptions
# Dev:  Neil McCracken
# Date:  May 13th, 2019
# ChangeLog: (Who, When, What)
#   NMcCracken 05/013/2019, Created Script

#-------------------------------------------------#
import pickle
#Data---------------------#
dictLineup=None
strPosition=None
strTerm=None
term=None

def GetLineup():
    '''Function get input and assigns those value to a dictionary'''
    value1 = input("Who is your starting Point Guard?: ")
    value2 = input("Who is your starting Shooting Guard?: ")
    value3 = input("Who is your starting Small Forward?: ")
    value4 = input("Who is your starting Power Forward?: ")
    value5 = input("Who is your starting Center?: ")
    myDict = {"Point Guard": value1, "Shooting Guard": value2, "Small Forward":value3,"Power Forward": value4,
            "Center": value5}
    return myDict


def Lookup_Posistion(word,lineup):
    '''Function to lookup a specific position and returns that name'''
    try:  # 'Try statement to catch an error
        return lineup[word]
    except KeyError:  # ''Exception generated if a invalid dictionary key is entered
        print("Not a valid position")
    finally:
        objfile.close()

try:
    print("Enter your basketball starting lineup\n")
    dictLineup=GetLineup()  # 'Function Call, catching return value
except NameError:  # 'To make sure function is correct
    print("Function not found.")
    exit()

objfile=open("lineup.dat", "wb") # 'writing to a binary file, overwriting contents
pickle.dump(dictLineup, objfile)  # 'pickling the object dictLineup
objfile.close()

objfile=open("lineup.dat", "rb")
dictLineup=pickle.load(objfile)  # 'Unpickling and assigning back to dictLineup
for k, v in dictLineup.items():  # 'Displaying lineup after unpickling
    print(k)
    print(v)

strTerm = input("\nEnter a position to look up your player. ")
strPosition=Lookup_Posistion(strTerm, dictLineup)  # 'Calling Function with two positional arguments and catching with variable
print(strPosition)
