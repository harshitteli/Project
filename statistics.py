import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,20,30,40,50]
plt.plot(x,y)
plt.title("Student hrs vs marks")
plt.xlabel("hrs")
plt.ylabel("marks")
plt.show()

subject=["M1","M2","M3","M4","M5"]
marks=["19","13","25","11","23"]
plt.bar(subject,marks)
plt.title("suject vs marks")
plt.xlabel("subject")
plt.ylabel("marks")
plt.show()

food_shops =[1,2,3,4]
area=["jamnagar","bhilwara","patna","jaipur"]
plt.pie(food_shops,labels=area)
plt.title("pie chart")
