count=1
while count<=5:
    print(count)
    count+=1
print()
count=5
while count>-1: print(count);count-=1
else:print("in else block")
print("out from loop")
print()
count=1
while count<=5:
    print(count)
    count+=1
    if count==4:
        break
else:print("in else block")
print()
num=int(input("enter a number (enter 0 to quit)"))
tot=0
while num!=0:
    tot+=num
    num = int(input("enter a number (enter 0 to quit)"))
print(tot)
