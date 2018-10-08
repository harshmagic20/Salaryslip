name=(input("Enter Employee Name: "))
id=(input("Enter Employee ID : "))
des=(input("Designation: "))
sal=int(input("Enter Basic Salary: " ))
leave=int(input("Enter No. Leave: "))

hra = 5*sal /100    
ta = 5*sal /100
da = 5*sal /100
a= leave*100
tax= 5*sal /100
gross= sal+hra+ta+da
salary=gross-a-tax

print("************Salary Slip****************")
print("Employee ID:", id)
print("Employee Name: ", name)
print("Designation: ", des)
print("**********Earnings**********")
print("Basic Salary: ",sal)
print("House Rent Allowance: ",hra)
print("Travelling Allowance: ",ta)
print("Dearness Allowance: ",da)
print("Salary (Gross): ",gross)
print("********Deductions***********")
print("Tax: ", tax)
print("Unpaid Leave: ", a)
print("NET Salary: ", salary)