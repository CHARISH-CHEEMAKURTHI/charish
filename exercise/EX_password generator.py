import random as rd
num=range(9)
count_num=int(input("how many numbers do you want?"))
a=rd.choices(num,k=count_num)
# print(a)
# print(type(a))
count_shapes=int(input("how many shapes do you want?"))
shapes=["~","!""@","#","$","%","^","&","*"]
b=rd.choices(shapes,k=count_shapes)
# print(b)
letters=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
count_letters=int(input("how many letters do you want?"))
c=rd.choices(letters,k=count_letters)
# print(c)
d=a+c+b
# print(d)
rd.shuffle(d)
# print(d)
password=""
for i in d:
    password+=str(i)
print()
print(f"your password is: \"{password}\"")

