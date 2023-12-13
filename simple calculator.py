#Arithmetic operators
#Addition(+)
#Subtraction(-)
#Division(/)
#Multiplication(*)
#Exponentiation(**)
#Modulus(%)
#floor division(//)
for x in range(3):
    print("="*50)
    print("#"*15,"WELCOME TO MY SIMPLE CALCULATOR","#"*15 )
    choice=input("choose operator +,-,/,*,**,%,//")
    num1=int(input("enter first num:"))
    num2=int(input("enter second num:"))
    if choice=="+":
        print(num1+num2)
    elif choice=="-":
        print(num1-num2)
    elif choice=="/":
        print(num1/num2)
    elif choice=="*":
        print(num1*num2)
    elif choice=="**":
        print(num1**num2)
    elif choice=="%":
        print(num1%num2)   
    elif choice=="//":
        print(num1//num2)
    else:
        print("invalid choice") 

