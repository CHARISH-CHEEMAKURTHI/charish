n=int(input())
s=int(input())
d=input()
a=0
b=0
c=0
if d=="L":
    c=n-s
    if s%2==0:
        b=a=s/2
    else:
        a=b=(s+1)/2
elif d=="R":
    a=n-(n-s)-1
    if (n-s)%2==0:
        b=c=(n-s)/2
    else:
        b=c=((n-s)+1)/2
print(f"{int(a)} {int(b)} {int(c)}")
