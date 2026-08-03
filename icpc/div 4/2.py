t=int(input("t :"))
for i in range(t):
    nmxy=input("n,m,x,y :").split()
    a=input("a :").split()
    b=input("b :").split()
    c=0
    for j in range(len(a)):
        c+=1
    d=0
    for j in range(len(b)):
        d+=1
    print(c+d)
