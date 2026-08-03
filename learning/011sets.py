set1={1,2,4.5,"abc",True,False,0}
set2={}
a=set()
print(set1)
print(type(set1))
print(type(set2))
print(type(a))
print(len(set1))
set1.add(3)
print(set1)
set1.remove(1)
print(set1)
set1.remove(0)
print(set1)
set1.discard(9)
print(set1)
#set1.remove(9)
#print(set1)
#set1.clear()
#print(set1)
print(set1.pop())
print(set1)
#we can add any tuple inside a set but we cant add a list to a set
#because set and tuple are immutable and liat is mutable
set1.add((1,2,3))
print(set1)
#set1.add([1,2,3])
set1={1,2,4.5,"abc",True,False,0}
print(len(set1))


