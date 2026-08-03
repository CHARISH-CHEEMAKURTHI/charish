n=int(input())
d=input()
if len(d)==n:
    l=d.count("L")
    r=d.count("R")
    if l>r:
        print("Left")
    elif l<r:
        print("Right")
    else:print("Beeline")