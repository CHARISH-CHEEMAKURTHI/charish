t=int(input("t :"))
for i in range(t):
    xn=input("x , n :")
    xn=xn.split()

    if int(xn[1])%2==1:
        print(int(xn[0]))
    else:print(0)