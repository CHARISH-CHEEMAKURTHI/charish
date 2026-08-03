mp = int(input("enter your money hiding place:"))

list1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
if mp == 11:
    list1[0][0] = "x"
elif mp == 12:
    list1[0][1] = "x"
elif mp == 13:
    list1[0][2] = "x"
elif mp == 21:
    list1[1][0] = "x"
elif mp == 22:
    list1[1][1] = "x"
elif mp == 23:
    list1[1][2] = "x"
elif mp == 31:
    list1[2][0] = "x"
elif mp == 32:
    list1[2][1] = "x"
elif mp == 33:
    list1[2][2] = "x"
else:
    print("wrong number")

a = list1[0]
b = list1[1]
c = list1[2]
print(f"{a}\n{b}\n{c}")