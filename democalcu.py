#python calculator
#Addition
#subtraction
#Multiplication
#Division
#Module
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
def mod(n1, n2):
    return n1%n2
a=int(input("Enter 1st number ="))
b=int(input("Enter 2nd number ="))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Module")
select=int(input("select any operation 1,2,3,4,5\n==>"))
if select == 1:
    print("addition=",a,"+",b,"=",add(a,b))
elif select ==2:
    print("subtraction=",a,"-",b,"=",sub(a,b))
elif select ==3:
    print("multiplication=",a,"*",b,"=",mul(a,b))
elif select ==4:
    print("Division=",a,"/",b,"=",div(a,b))
elif select ==5:
    print("Module=",a,"%",b,"=",mod(a,b))
else:
    print("INVALID INPUT")


    