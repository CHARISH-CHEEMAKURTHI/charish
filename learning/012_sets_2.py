set_1={"charish","anabelle","the nun","conjuring"}
set_2={"charish","triveni","janardhan rao","likhitha"}
set_3={"triveni","lavanya","kusuma kumari","subbarao"}
print(set_1.union(set_2))
print(set_1.union(set_2,set_3))
print(set_1 | set_2)
print(set_1 | set_2 |set_3)
print(set_1.union(["snow anna" , "snow uncle"]))
#print(set_1 | ["snow anna" , "snow uncle"])
set_1.update(set_3)
print(set_1)
set_2|=set_3
print(set_2)
set_1={"charish","anabelle","the nun","conjuring"}
set_2={"charish","triveni","janardhan rao","likhitha"}
set_3={"triveni","lavanya","kusuma kumari","subbarao"}
print(set_1.intersection(set_2))
print(set_1.intersection(set_2,set_3))
print(set_1 & set_2)
print(set_1 & set_2 & set_3 )
print(set_1.intersection(["snow anna" , "snow uncle"]))
# print(set_1 & ["snow anna" , "snow uncle"])
set_1.intersection_update(set_2)
print(set_1)
set_2.intersection_update(set_3)
print(set_2)
