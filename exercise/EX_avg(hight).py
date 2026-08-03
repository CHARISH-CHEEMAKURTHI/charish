heights=input("enter all heights:")
height=heights.split(",")
h=list(height)
print(h)
H=[]
for i in h:
    print(i)
    a=int(i)
    H.append(a)
    if len(H)==2:
        H=[H[0]+H[1]]
print(H)
b=H[0]
print(b)
n=0
for c in h:
    n+=1
print(n)
d=b/n
print(d)
avg=round(d)
print("the average of all your heights is" , avg)


