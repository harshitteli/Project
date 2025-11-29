# Project
def divide():
    if b!=0:
     print("Divide :",a/b)
    else:
     print("invalid operation")
        
while  1==1:
 print("Calulator")
 wanting=input("Do you want to use it:")
 if wanting =="yes":
     a=float(input("Enter the first number"))
     b=float(input("Enter the second number"))
     operation=input("enter operation")
     if operation == "+" :
      print(a+b)
     else :
      if operation == "-":
       print(a-b)
      else :
        if operation == "*":
          print(a*b)
        else :
          if operation == "/":
            divide()
          else:           
            print("invalid operator")
 else:
    if wanting=="no":
      print("exit from calculator")
      break
    else:
      print("invalid answer")
