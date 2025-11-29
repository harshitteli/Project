Amount=80000
pin=1234
user_id="harshit"
attempts=1
while 1==1:
 p=input("enter your id:")
 if p==user_id:
    q=int(input("enter your pin:"))
    if q==pin:
       h=input("what you want to do (deposit or witdraw)?:")
       if h=="withdraw":
          withdraw = int(input("enter amount to withdraw"))
          print("new amount is :",Amount-withdraw)
          print(f"{withdraw} is withdrawn from your account")
       else:
          if h=="deposit":
           deposit=int(input("enter amount to deposit:"))
           print("new amount:",Amount+deposit)
           print(f"{deposit} is deposited in your account")
          else:
           print("inavalid action")
    else:
      print("invalid pin")
      print("attempts remaining:",3-attempts)
      attempts+=1
      q=int(input("enter your pin:"))
      if q==pin:
        h=input("what you want to do (deposit or witdraw)?:")
        if h=="withdraw":
          withdraw = int(input("enter amount to wihdraw"))
          print("new amount is :",Amount-withdraw)
          print(f"{withdraw} is withdrawn from your account")
        else:
          if h=="deposit":
           deposit=int(input("enter amount to deposit:"))
           print("new amount:",Amount+deposit)
           print(f"{deposit} is deposited in your account")
          else:
           print("inavalid action")
      else:
         print("invalid pin")
         print("attempts remaining:",3-attempts)
         attempts+=1
         q=int(input("enter your pin:"))
         if q==pin:
          h=input("what you want to do (deposit or witdraw)?:")
          if h=="withdraw":
           withdraw = int(input("enter amount to wihdraw"))
           print("new amount is :",Amount-withdraw)
           print(f"{withdraw} is withdrawn from your account")
          else:
           if h=="deposit":
            deposit=int(input("enter amount to deposit:"))
            print("new amount:",Amount+deposit)
            print(f"{deposit} is deposited in your account")
           else:
            print("inavalid action")
         else:
           print("invalid pin , now your id is temporily blocked")
           break
 else:
    print("invalid user id")


    
