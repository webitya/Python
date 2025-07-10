# Write a Program to Print all the data using Recursion


index=0


def PrintData(data):
    global index
    length=len(data)
    if(index<length):
        print(data[index])
        index+=1
        PrintData(data)
    else:
        pass    
     




# PrintData(["Aditya","Aditya01","Aditya02","Aditya03","Aditya01"])


# Write a Program to match the input text  and match it to the list
index=0
count=0
def Find(data,name):
     global index
     global count
     length=len(data)
     if(index<length):
         if(name==data[index]):
             count+=1
             index+=1         
             return Find(data,name)
         else:
             index+=1
             return Find(data,name)
     else:
         return f'{name} occurs {count} times in the data list'             
             

def App(name):
    data=["Aditya","Karan","Nagwanshii","Aditya01","Aditya"]
    return Find(data,name)


name=input("Enter Name You Want TO Search : ")
print(App(name))        

