N=int(input("no.of rows:"))

if N%2==0:
    N=N//2
    for i in range(N):
        print("p"*4)
    for i in range(N):
        print("p"*2)
elif N%2!=0:
    for i in range(round(N/2)):
        print("p"*4)
    for i in range(round(N/2)):
        print("p"*2)

N = int(input("no.of rows:"))
for i in range(N):
    print(" "*i,"g"*N)
    N=N-1
