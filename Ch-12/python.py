# Write a Python Program to find the index of an element or item using list

index=0
count=0
def FindIndex(data,element):
    global index
    global count
    length=len(data)
    if(index < length):
        if(data[index]==element):
           count += 1
           index += 1
           return FindIndex(data,element)
        else:
           index += 1
           return FindIndex(data,element)
    else:
        return f'{element} in data list apppears {count} times'      
 

def App():
    data=["Aditya01","Aditya02","Aditya03","Aditya04","Aditya05","Aditya01"]
    element=input("Enter Eleement You Want To Search : ")
    return FindIndex(data,element)

a = App()
print(a)

