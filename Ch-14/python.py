
# def Test():
#     for index in range(1,21,2):
#         print("Aditya Kumar : ", index)
# Test()      

# def Table(num):
#     for index in range(1,11,1):
#         print(f'{num} x {index} = {num*index}')


# num=int(input("Enter the number : "))
# Table(num)

# COUNT DOWN TIMER

from time import sleep as Timer

def CountDown():
    for index in range(10,-1,-1):
        Timer(1)
        print(index)
    Timer(2)    
    print("Mission Completed!")    
CountDown()        