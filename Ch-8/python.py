
# def output(data,char):
#     data=data
#     dataLength=len(data)
#     return (f'The First Charact Of the String is {data[0]} and the last Charcter is {data[dataLength-1]}')
#     return dataLength,data[char],"Last Character : "+data[dataLength-1]

# data=input("Enter any String Data : ")
# char=int(input("What Index You Want from Input data : "))
# print(output(data,char))


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


# print(characterFinder())


# Question:

# Create a function check_positive
# Pass value to the function by taking user input
# If value is Positive, print it. Else print Negative.

def check_positive(val):
    if(val>=0):
        return "Positive"
    else:
       return "Negative"


# val=int(input("Enter Any Number : "))
# print(check_positive(val))

# Write a program to print the largest of the three numbers.

def largestNumber(a,b,c):
    if(a>b and a>c):
        return f'a = {a} is largest than {b} and {c}'
    elif(b>c and b>a):
        return f'b = {b} is largest than {a} and {c}'
    else:
        return f'c = {c} is largest than {a} and {b}'


a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))

print(largestNumber(a,b,c))