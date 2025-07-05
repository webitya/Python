# Character Finder || Application
def firstCharacter(data):
    data=data
    return(f'Your Data is "{data}" and your first character is :- {data[0]}')

def lastCharacter(data):
    data=data
    length=len(data)
    return f'Your data is "{data}" and your last character is :- {data[length-1]}'

def customCharacter(data):
    data=data
    length =len(data)
    custom=int(input("Enter Which Index Character You Want To Find : "))
    if(custom<length):
        return f'Your data is "{data}" and your choosen index is "{custom}" so your "{custom} character" is :- {data[custom]}'
    else:
        return "Index Not Found"


def characterFinder():
    print("------CHARACTER FINDER APPLICATION-------\n")
    data=input("Enter Any String You Want : ")
    print(f'Your Data is :  {data} ')
    print("Choose Option You Want :- ")
    print("Option 1 :- Find First Character ")
    print("Option 2 :- Find Last Character ")
    print("Option 3 :- FInd Custom Character ")
    print("------------------------------------------")
    option=int(input("Enter Your Option :- "))
    if(option == 1):return firstCharacter(data)
    elif(option ==2):return lastCharacter(data)
    elif(option ==3):return customCharacter(data)
    else:print("Option Not Found Try Again")


print(characterFinder())