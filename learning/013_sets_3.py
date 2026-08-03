set_1={"charish","anabelle","the nun","conjuring"}
set_2={"charish","triveni","janardhan rao","likhitha"}
set_3={"triveni","lavanya","kusuma kumari","subbarao"}
print(set_1.difference(set_2))
print(set_2.difference(set_1 ,set_3))
print(set_1.difference(["snow anna" , "snow uncle"]))
print(set_1 - set_2)
print(set_2-set_1-set_3)
# print(set_1 - ["snow anna" , "snow uncle"])
set_1.difference_update(set_2)
print(set_1)
print(set_2)
set_1={"charish","anabelle","the nun","conjuring"}
print(set_1.symmetric_difference(set_2))
print(set_1.symmetric_difference(["snow anna" , "snow uncle"]))
# print(set_1.symmetric_difference(set_2,set_3))
print(set_1^set_2^set_3)
# print(set_1^["snow anna" , "snow uncle"])
set_1.symmetric_difference_update(set_2)
set_2.symmetric_difference_update(["snow anna" , "snow uncle"])
print(set_1)
print(set_2)