h=float(input("enter your height"))
bill=0
if h>3.0:
    print("yes you can ride")
    age = int(input("please enter your age"))
    if age<12:
        print("your ticket price is 200 .rs")
        bill=200
    elif 12>=age>18:
        print("your ticket price is 350.rs")
        bill=350
    else:
        print("your ticket price is 500.rs")
        bill=500
    print("photo prise is 50.rs")
    p=input("do you want any photos(yes/no)?")
    if p=="yes":
        bill+=50
    time=int(input("how many minutes you want to ride(10/15/20/25)? "))
    if time==10:
        bill+=50
        print(f"your total ticket price is {bill} .rs ")
    elif time==15:
        bill+=75
        print(f"your total ticket price is {bill} .rs ")
    elif time==20:
        bill+=100
        print(f"your total ticket price is {bill} .rs ")
    else:
        bill+=125
        print(f"your total ticket price is {bill} .rs ")
else:
    print("sorry you can`t ride")
print("thank you")

