set_1={1,2,3,4,5,6,7,8,9,10}
set_2={3,4,5,6,7}
set_3={11,12,13,14,15}
print(set_2.isdisjoint(set_3))
print(set_1.isdisjoint(set_2))
print(set_2.isdisjoint(set_1))
print(set_1.issubset(set_2))
print(set_2.issubset(set_1))
print(set_1 <= set_2)
print(set_1.issuperset(set_2))
print(set_2.issuperset(set_1))
print(set_1 >= set_2)