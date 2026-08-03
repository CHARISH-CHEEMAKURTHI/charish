import random as r

names=input("enter every body`s name separated by coma:")
a=names.split(",")
print(a)
b=len(a)
c=r.randint(0,b-1)
print(f"{a[c]}will pay the bill")