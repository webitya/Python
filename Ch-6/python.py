
def PercentageFinder():
    amount=input("Enter The Amount")
    print("The Amount Is ",amount)
    percentage=input("Enter The Percentage")
    print("The Percentage Is",percentage)
    result=(int(amount)*int(percentage))/100
    return "The ",percentage, "percent of ",amount," is ",result


# print(PercentageFinder())

def Percentage(amount,percent):
    amount=amount
    print("The amount is ", amount)
    percent=percent
    print("The Percent is ",percent)
    result = (amount*percent)/100
    print(percent,"% of ",amount," is ",result)

# Percentage(200,10)

def WagesCalculator(name,Month,Days,MonthlySalary):
    noOfDaysInAMonth=Month*30
    TotalNoOfPresentDays=Days
    SalaryOfOneDay=MonthlySalary/noOfDaysInAMonth
    ReceiveableAmount=SalaryOfOneDay*TotalNoOfPresentDays
    print(name,"Your Monthly Salary is ",MonthlySalary , "You are Present for ",TotalNoOfPresentDays, "So Your Receiveable amount is ",ReceiveableAmount)

# WagesCalculator("Siya",1,13,3000)
# WagesCalculator("Alan",1,15,1500)
# WagesCalculator("Piyush",1,7,1500)

def loopCreator(content,num):
    print(content  *num)
# loopCreator("10\n",3)    

def loopCreator1():
    data=str(input("Enter Your Data \n "))
    num=int(input("Enter Your Number \n"))
    print(str('Result '+'\t'+'\t'+'='+'\t'+data+'\n')*num)
loopCreator1()    


