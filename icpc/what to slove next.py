l1=input()
l1=l1.split()

solved=[0]*int(l1[1])
tried=[0]*int(l1[1])
incorrect=[0]*int(l1[1])

for i in range(int(l1[0])):
    l = input()
    l = l.split()
    for j in range(int(l1[1])) :
        sign=l[2*j]
        num=int(l[2*j+1])
        if sign=='+': solved[j] += 1
        if sign=='+' and num>0 : tried[j] +=1
        incorrect[j] +=num
for i in range(int(l1[1])):
    print(solved[i], tried[i] ,incorrect[i])
