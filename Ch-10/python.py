# Ternary Operaor 

result="Adult" if 30>=20 else "Minor"
# print(result)


def printGrade(marks):
    # Write your code here using a switch statement to print the grade based on marks
    if marks >= 90 : print("Grade:A")
    elif marks >= 80 and marks<=89 : print("Grade:B")
    elif marks>=70 and marks<=79 : print("Grade:C")
    elif marks>=60 and marks<=69 : print("Grade:D")
    else : print("Grade:E")


# score=int(input())
# printGrade(score)


# i=1  Starting 
# while i<=10:  Keyword/Stoping   
#     print(i) logic 
#     i+=1   Beheviour


# Optional Paramenter

def Add(x=0,y=3):
    z=x+y
    return z



def App():
    result=Add(5)
    print("The addition is : ",result)
# App()    


# Recurision
index=0
def Message():
    global index
    index+=1
    if(index<=20):
         print(index,"Message")
         Message()
    else:
        print("Ended")     
# Message()


# Table Of 10

index=1
def Table(a):
    global index
    if(index<=10):
        print(f'{a} x {index} = {a*index}')
        index+=1
        Table(a)
    else:
        pass

Table(30)

