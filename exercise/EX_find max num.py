numbers=input("enter numbers  separating with ',':")
a=numbers.split(",")
num=list(a)
print(num)
n=[]
for i in num:
    b=int(i)
    n.append(b)
print(n)
maxi=n[0]
for c in n:
    if c>maxi :
        maxi=c
print("the maximum number is ",maxi)