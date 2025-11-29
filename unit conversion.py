def divide():
    if b!=0:
     print("Divide :",a/b)
    else:
     print("invalid operation")
try:
 while True:
  wanting=input("Do you want to use it:")
  if wanting =="yes":
   ans=input("enter use")
   if ans=="Temperature":
     b=input("unit of base temperature")
     v=float(input("value of base temperatue"))
     c=input("unit of converted temperature")
     if b=="celsius" :
      if c=="fahrenheit" :
       print("conversion of value in farenheit :",9/5*v+32)
      else:
       if c=="kelvin" :
        print("conversion of value in kelvin :",100+v)
       else:
        print("invalid chose")
     else:
      if b=="fahrenheit" :
       if c=="celsius" :
        print("conversion of value in celsius :",5/9*(v-32))
       else:
         if c=="kelvin" :
          print("conversion of value in kelvin :",100+5/9*(v-32))
         else:
          print("invalid chose")
      else:
       if b=="kelvin" :
        if c=="celsius" :
         print("conversion of value in celsius :",v-100)
        else:
           if c=="fahrenheit" :
            print("conversion of value in fahrenheit :",9/5*(v-100)+32)
           else:
            print("invalid chose")
       else:
        print("invalid chose") 
           
   else:
    if ans=="Calculator":
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
       if ans=="Distance":
        p=input("enter base unit of distance:")
        q=float(input("enter value of distance to convert:"))
        r=input("enter unit of distance to convert:")
        if p=="cm" :
         if r=="m" :
          print("conversion of value in metre :",100*q)
         else:
          if r=="km" :
           print("conversion of value in kilometre :",100000*q)
          else:
           print("invalid chose")
        else:
         if p=="m" :
          if r=="cm" :
            print("conversion of value in centimetre :",q/100)
          else:
           if r=="km" :
            print("conversion of value in kilometere :",q*1000)
           else:
            print("invalid chose")
         else:
          if p=="km" :
           if r=="cm" :
            print("conversion of value in centimetre :",q/100000)
           else:
            if r=="m" :
             print("conversion of value in metre :",q/1000)
            else:
             print("invalid chose")
          else:
           print("invalid chose")
       else:
        print("invalid choice")
  else:
   if wanting=="no":
      print("exit......")
      break
   else:
      print("invalid answer")
except:
    print("resolving error")


