# Write a Python Program to find the index of an element or item using list


from testchild import FindIndex



def App():
    data=["Aditya","aditya01","aditya02","aditya03","aditya04"]
    name=input("Enter Your Name : ").lower().strip()
    return FindIndex(name,data)

print(App())      