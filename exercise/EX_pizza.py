print("we have 3 size of pizza in our stor")
print("they are small/medium/big")
size=input("which size do you want?")
if size=="small":
    print("price of small pizza is 100.rs")
    bill=100
    a = input("do you want pepperoni(y/n)")
    if a == "y" or a == "Y":
        print("30.rs")
        bill += 30
elif size=="medium":
    bill=200
    print("price of medium pizza is 200rs")
    a= input("do you want pepperoni(y/n)")
    if a == "y" or a == "Y":
        bill += 50
        print("50.rs")
else :
    bill=300
    print("price of large pizza is 300.rs")
    a = input("do you want pepperoni(y/n)")
    if a == "y" or a == "Y":
        bill += 50
        print("50.rs")
a=input("do you want extra cheese (y/n)")
if a=="y" or a=="Y" :
    print("extra cheese for any pizza is 20.rs")
    bill+=20
print(f"your total bill is {bill} ")