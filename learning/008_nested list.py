#nested list

list1=[1,112,23,45,-90,[],[1,2.3,"abc",False]]
print(len(list1))
print(list1[5])
print(list1[6])
print(list1[6][0])
print(list1[6][1])
print(list1[6][2])
print(list1[6][3])
print(list1[6][len(list1[6])-1])
print(list1[6][::])
print(list1[6][0:])
print(list1[6][:4])
print(list1[6][0:4:2])
