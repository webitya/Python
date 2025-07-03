def add_five(num):
    return 5+num


# val=int(input("Enter Number \t=\t"))
# result=add_five(val)
# print(result)


def checkDataType():
    data=input("Enter any Data")
    return type(data).__name__

# print(checkDataType())


# Comparision Operator

def call():
    result =10==10
    return result

# print(call())


# Conditions

if (10==11):
    print("Aditya")

else :
    print("Aditya Kumar")   


#Age Checker
def canVote():
    age=int(input("Enter Your Age : "))
    if(age>18):
        return "Adult"
    elif (age>12 and age<=18) :
        return "Teenager"
    else:
        return "Child"

# print(canVote())


def checkPassword():
    password=input("Enter Strong Password atleast 8 Character : ")
    length=len(password)
    if(length>=8):
        return "Success"
    else:
        return "Password at least 8 Character"

print(checkPassword()) 


    

