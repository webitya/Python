# Jis Foldder ke andar saara module ka collection hota hai ussi ko package bolte hai lib folder
# User Define Module | Built in Module | Third Party Module
# from  lib.output import output
# def Main():
#     output()
# Main()    


# Bilt in Module Example
# import time
# from time import sleep as sl
# def Main():
#     print("One")
#     sl(5)
#     print("Two")
#     sl(5)
#     print("Three")
# Main()    

from time import sleep as timer
from lib.output import output as Result
index =10

def RocketLaunch():
    global index
    if(index>0):
        index -= 1
        timer(1)
        Result(index)
        RocketLaunch()
    else:
        timer(2)
        Result("ROcket Launch Successfully")    
RocketLaunch()        

        

    