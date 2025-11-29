ticket=input("Do you have ticket?")
if ticket=="yes":
    age=int(input("Enter your age"))
    if age>18:
        print("you can enjoy movie")
    else :
       if age>15 & age<18:
           print("you can watch movie but with your parents")
       else:
           print("you are not eligible")

else:
    if ticket=="no":
       print("purchase ticket first!!!")
    else:
        print("sahi se bata de")
